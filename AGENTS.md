# VD Newton Project Guidance

## Project responsibility

This workspace is the Newton entry-production surface. Its primary job is to
translate managed VD context and analysis into entry packets, actual Newton
entries, and trace/evaluator checks. It does not own the organization or
maintenance of the NML document collection.

## Repository access and boundaries

The private GitHub repository `canvalidk/VD-Newton` is the backing repository
for this workspace. Its local `origin` points there, and the installed GitHub
connector has confirmed read/write access. Use that repository for normal
workspace commits and pushes, while still verifying the current remote and
authentication before a write.

`VDfirst/` is a separate local checkout of `canvalidk/VDfirst`. It is excluded
from VD-Newton and must not be staged, committed, or pushed as part of this
workspace. Do not write or push to `canvalidk/VDfirst` unless the user explicitly
asks for work on that repository.

Repository access does not change the context boundary below:
`canvalidk/VD-docs` remains the managed-context authority, while VD-Newton owns
the active Newton entry-production surface.

## VD-docs is the managed-context authority

The private GitHub repository `canvalidk/VD-docs` is the default source for VD
document discovery and current **managed** context. Use the installed GitHub
connector to read it. VD-docs is not necessarily exhaustive: this workspace
may contain active or newly created notes that have not yet been submitted to
the VD Folders inbox or organized into the managed collection.

For requests such as "find the document", "what have we said about X?", "tell
me everything pertaining to X", or other VD context/analysis questions:

1. Consult `canvalidk/VD-docs` automatically rather than assuming the answer
   must be found locally. Also inspect active local material when completeness,
   recency, or unsubmitted work may matter.
2. Treat `catalog.yaml` as the inventory and organization authority for the
   managed collection. Absence from the catalog is not evidence that no local
   or not-yet-ingested document exists.
3. For substantive work, resolve one `main` commit and read all task sources at
   that commit so the context is a coherent snapshot.
4. Fetch only the relevant canonical files and follow their `informs` links,
   source references, and context-bundle references as needed.
5. For broad or exhaustive synthesis, distinguish managed/current,
   managed/historical, inbox/unclassified, and local active/unsubmitted
   material. Report the commit, local scope, files inspected, search terms or
   selection method, and any coverage limitations.

Do not assume local NML, Newton-analysis, or Theory copies are current merely
because they are easier to access: they may be historical snapshots. Do not
assume they are stale merely because VD-docs has no matching record either:
they may be newer or unsubmitted. Determine and report their relationship. If
the GitHub connector is unavailable, say so and label the managed-context
coverage as unverified.

## Local authority and agency

Use local files first for active implementation surfaces: entry packets,
current Newton entry drafts, engine/code, trace tests, evaluator work, and
quick scoped changes needed to advance entry production.

Managed VD-docs context is read-only by default. Do not reorganize, rename,
deduplicate, refresh, or edit NML/context/informing documents in VD-docs unless
the user explicitly asks. Record important conflicts, stale sources, entry
decisions, and newly discovered dependencies as a handoff to the VD folders
manager instead.

Do not delete, archive, or demote a local document solely because a copy exists
in VD-docs. First establish whether the local file is historical, current,
unsubmitted, or divergent and whether the managed copy has actually absorbed
its content.

When an entry task consumes VD-docs context, record the repository commit and
source paths in the entry packet or handoff. Store locally the entry-facing
interpretation and decisions, not another maintained copy of the source
collection.

## Outbound handoffs to VD-docs

User policy established 2026-09-05: save new records and handoff documents
intended for VD-docs in the workspace-root folder `pass to VD-docs/`.
This is the local staging location for documents awaiting transfer to the
managed collection. Keep their source references and submission status in
the document; saving there does not itself mean VD-docs has received it.

Active entry packets, drafts, engine/code, and evaluator work remain on their
normal production surfaces. Apply this handoff policy to new documents and
documents the user identifies for transfer; do not bulk-move historical
handoffs solely because the new policy exists.
