# Newton Design 3

Design 3 will develop Newton entries by running mechanics questions end to end with explicitly supplied inputs. Start with one question and follow it to a result. Where the trace stalls or someone has to supply a step, use that point to decide which entry to write next. For force summation, follow how the trace selects each interaction, adds its force, and reaches the end of the sum.

Use the first working traces for later conceptual analysis. The proposed Design 4 work covers how parameters get their values and how witness sheets support the answers supplied to a trace.

- [Entry structure](DESIGN_3_ENTRY_STRUCTURE.md) tracks proposed entries and their roles.
- [Official Python dictionary](newton_design_3.py) holds the ordered entry strings and the VDfirst builder. It starts empty.
