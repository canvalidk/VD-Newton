"""Official entry strings for Newton Design 3. Load with VDfirst on the Python path."""

from engine import VDInstance


# Append one (headword, definition) pair per entry, in dictionary order.
NEWTON_ENTRIES: list[tuple[str, str]] = [
    # K1
    (
        "time",
        "A background ordering value, usually modelled by t ∈ R; a time-value selects\n"
        "an instant, and the difference between two time-values is a duration.",
    ),
    # K2
    (
        "reference-frame",
        "A convention for assigning spatial and temporal coordinates to events using an\n"
        "origin, basis vectors, and a clock.",
    ),
    # K3
    (
        "displacement",
        "A spatial vector with units of length, expressed in a chosen reference-frame.",
    ),
    # K4
    (
        "straight-line",
        "A geometric locus in a reference-frame whose displacement-vectors have the form\n"
        "r0 + λu, with r0 fixed, u nonzero, and λ real.",
    ),
    # K5
    (
        "path",
        "A timeless spatial locus or form in a reference-frame.",
    ),
    # K6
    (
        "time-interval",
        "A selected span of time from a start-time to an end-time over which a motion\n"
        "description is considered.",
    ),
    # K7
    (
        "point-particle",
        "An idealised object whose spatial extent and internal structure are neglected\n"
        "for the motion description.",
    ),
    # K8
    (
        "trajectory",
        "For a point-particle in a reference-frame over a time-interval, a time-indexed\n"
        "map from selected time-values to displacement-vectors in that frame.",
    ),
    # K9
    (
        "position",
        "For a point-particle with a trajectory, the displacement-vector returned by that\n"
        "trajectory at a selected time in the chosen reference-frame.",
    ),
    # K10
    (
        "velocity",
        "For a point-particle with a trajectory in a reference-frame, the derivative of\n"
        "that trajectory with respect to time at a selected time, when that derivative\n"
        "exists.",
    ),
    # K11
    (
        "speed",
        "For a point-particle at a selected time in a reference-frame, the scalar\n"
        "magnitude of its velocity.",
    ),
    # K12
    (
        "acceleration",
        "For a point-particle in a reference-frame, the derivative of velocity with\n"
        "respect to time at a selected time; equivalently, the second derivative of the\n"
        "trajectory, when defined.",
    ),
    # K13
    (
        "relative-position",
        "For two point-particles in the same reference-frame at the same selected time,\n"
        "the displacement-vector r2 - r1 obtained by subtracting the first position from\n"
        "the second.",
    ),
    # K14
    (
        "relative-velocity",
        "For two point-particles in the same reference-frame at the same selected time,\n"
        "the derivative of relative-position with respect to time; equivalently, the\n"
        "second velocity minus the first, when defined.",
    ),
    # K15
    (
        "path-length",
        "The length of a piecewise smooth path in a reference-frame is the integral of "
        "the spatial line element along the path, counting each arc once.",
    ),
    # K16 / E1
    (
        "uniform-motion",
        "A frame-indexed interval property of a point-particle: over the selected\n"
        "time-interval, its trajectory either stays at one position in the chosen frame,\n"
        "or traces a straight path with constant velocity, i.e. constant speed with\n"
        "unchanged direction.",
    ),
    # E2
    (
        "uniform-motion",
        "Uniform-motion is the motion a free-particle must exhibit when described in an "
        "inertial-frame.",
    ),
    # E3
    (
        "inertial-frame",
        "A reference-frame in which every free-particle must exhibit uniform-motion.",
    ),
    # E4
    (
        "free-particle",
        "A point-particle that must exhibit uniform-motion when described in an "
        "inertial-frame.",
    ),
    # E5
    (
        "inertial-frame",
        "A reference-frame modelled, to the required accuracy, as introducing no "
        "acceleration through its own translation or rotation.",
    ),
    # E6
    (
        "free-particle",
        "A point-particle whose trajectory is uninfluenced by other objects. It may "
        "represent a material-object or a massless particle such as a photon.",
    ),
]


def build_newton_instance() -> VDInstance:
    """Build a fresh Design 3 dictionary from the entries in this file."""
    dictionary = VDInstance(name="Newton Design 3")
    dictionary.append_many(NEWTON_ENTRIES)
    return dictionary
