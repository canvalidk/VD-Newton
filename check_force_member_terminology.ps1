param()

$ErrorActionPreference = 'Stop'

$repoRoot = $PSScriptRoot
$bundledRg = Join-Path $repoRoot '.tools\rg.exe'
if (Test-Path -LiteralPath $bundledRg) {
    $rg = $bundledRg
} else {
    $rgCommand = Get-Command 'rg' -ErrorAction SilentlyContinue
    if (-not $rgCommand) {
        throw 'ripgrep (rg) is required to run the force-member terminology check.'
    }
    $rg = $rgCommand.Source
}
$pattern = '(?<![A-Za-z0-9])(?:contributing|attached|acting)[- ]force(?:s|\|s)?(?![A-Za-z0-9])'

$allowedGlobs = @(
    '!VDfirst/**',
    '!.git/**',
    '!**/*.backup-*.md',
    '!07_design_2_1/notes/conversation_captures/**',
    '!07_design_2_1/notes/vd_docs_handoffs/**',
    '!07_design_2_1/entry_writing_passes/**',
    '!08_nm_lesson_drafts/nml3/NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md',
    '!08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md',
    '!08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md'
)

$arguments = @('--pcre2', '-n', '-i', '--hidden')
foreach ($glob in $allowedGlobs) {
    $arguments += @('--glob', $glob)
}
$arguments += @($pattern, '.')

Push-Location $repoRoot
try {
    $matches = & $rg @arguments 2>&1
    $rgExit = $LASTEXITCODE
} finally {
    Pop-Location
}

if ($rgExit -eq 0) {
    Write-Error @"
Obsolete force-member terminology remains on an active surface.
The sole active headword is impressed-force. Matches:
$($matches -join [Environment]::NewLine)
"@
    exit 1
}

if ($rgExit -gt 1) {
    Write-Error "Terminology scan failed: $($matches -join [Environment]::NewLine)"
    exit $rgExit
}

$obsoleteDecisionPattern = 'NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02\.md'
$decisionArguments = @('--pcre2', '-n', '--hidden')
foreach ($glob in @(
    '!VDfirst/**',
    '!.git/**',
    '!**/*.backup-*.md',
    '!07_design_2_1/notes/conversation_captures/**',
    '!07_design_2_1/notes/vd_docs_handoffs/**',
    '!07_design_2_1/entry_writing_passes/**',
    '!07_design_2_1/SOURCE_STATUS.md',
    '!check_force_member_terminology.ps1',
    '!08_nm_lesson_drafts/nml3/NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md',
    '!08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md'
)) {
    $decisionArguments += @('--glob', $glob)
}
$decisionArguments += @($obsoleteDecisionPattern, '.')

Push-Location $repoRoot
try {
    $obsoleteDecisionMatches = & $rg @decisionArguments 2>&1
    $decisionExit = $LASTEXITCODE
} finally {
    Pop-Location
}

if ($decisionExit -eq 0) {
    Write-Error @"
An active surface still points to the superseded terminology decision.
Replace it with NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md:
$($obsoleteDecisionMatches -join [Environment]::NewLine)
"@
    exit 1
}

if ($decisionExit -gt 1) {
    Write-Error "Superseded-decision scan failed: $($obsoleteDecisionMatches -join [Environment]::NewLine)"
    exit $decisionExit
}

$historicalFiles = @(
    $(Get-ChildItem (Join-Path $repoRoot '07_design_2_1\notes\conversation_captures') -File -Filter '*.md')
    $(Get-ChildItem (Join-Path $repoRoot '07_design_2_1\notes\vd_docs_handoffs') -Recurse -File -Filter '*.md')
    $(Get-ChildItem (Join-Path $repoRoot '07_design_2_1\entry_writing_passes') -File -Filter '*.md')
    $(Get-ChildItem $repoRoot -File -Filter '*.backup-*.md')
) | Where-Object {
    Select-String -LiteralPath $_.FullName -Pattern $pattern -Quiet
}

$unquarantined = foreach ($file in $historicalFiles) {
    $firstLine = Get-Content -LiteralPath $file.FullName -TotalCount 1
    if ($firstLine -ne '# HISTORICAL TERMINOLOGY QUARANTINE') {
        $file.FullName
    }
}

if ($unquarantined) {
    Write-Error @"
Historical files contain obsolete force-member terminology without the required
quarantine banner:
$($unquarantined -join [Environment]::NewLine)
"@
    exit 1
}

Write-Output 'PASS: impressed-force is the sole active force-member headword; historical occurrences are quarantined.'
