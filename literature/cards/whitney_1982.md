# Quasi-Static Assembly of Compliantly Supported Rigid Parts

## Metadata

**Authors:** D. E. Whitney

**Year:** 1982

**arXiv:** None

**Published venue:** *Journal of Dynamic Systems, Measurement, and Control* 104(1), 65–77

**DOI:** [10.1115/1.3149634](https://doi.org/10.1115/1.3149634)

**Publication status:** PUBLISHED

**READING_STATUS:** PARTIAL

**Source URL:** [ASME article PDF](https://asmedigitalcollection.asme.org/dynamicsystems/article-pdf/104/1/65/5777806/65_1.pdf); [CiteSeerX text record](https://citeseerx.ist.psu.edu/document?doi=f4f7faf5480dd8645146eba58330439862ced921&repid=rep1&type=pdf)

**Evidence role:** CORE

## Scientific question

How do geometry, support compliance, and contact friction determine force, error tolerance, and jamming during quasi-static mating of nominally rigid parts, and how should a Remote Center Compliance (RCC) be selected?

## Exact system and regime

Analytical model: planar round peg/round chamfered-hole insertion, represented as flat tabs and slots; small-angle approximations; constant, identical friction coefficient at all contacts; rigid parts relative to their supports. Support is modeled by lateral and angular springs, with a compliance center located a distance from the peg tip. Gravity and inertia are omitted. Experimental verifications use three-dimensional parts. [Introduction, p. 65]

## Main claims

### Compliance, geometry, and friction govern error-corrupted rigid-part mating

**OBSERVATION:** The paper derives geometric and static force-equilibrium conditions, plus insertion-force models, for chamfer crossing, one-point contact, and two-point contact in the stated planar peg–hole/spring model. Its abstract reports experimental verification of insertion-force behavior. [Abstract; Introduction and Fig. 1, p. 65]

**AUTHOR INTERPRETATION:** Part geometry, stiffness of the supporting jig/gripper, and inter-part friction are the major factors governing rigid-part mating; derived conditions can guide compliant-support design and increase successful assembly without pre-eliminating errors or sensing and correcting them during mating. [Introduction, p. 65]

**INFERENCE:** Within the idealized quasi-static regime, passive compliance can be treated as a design variable that changes the contact-force path and therefore the risk of unsuccessful insertion.

**Intervention or measurement:** Analytical variation of part geometry, support stiffness/compliance-center parameters, friction, and initial misalignment; experimental comparison of insertion-force behavior using 3-D parts.

**Observed result:** The accessible paper text states that the force models were verified experimentally; detailed numerical agreement, sample counts, and apparatus specifications were not inspected.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Same/constant friction assumed at every contact in the model; planar derivation is compared with experiments using 3-D parts. Further controls are not recoverable from the inspected text.

**Alternative explanations not excluded:** Dynamic effects, gravity, unequal or varying friction, surface deformation, and departures from small-angle geometry can affect actual insertion forces.

**Scope limitations:** Rigid parts; quasi-static support behavior; planar analytic representation; chamfered round peg/hole case; 3-D validation details unavailable in inspected material.

**Source pointer:** Abstract; §1 Introduction, p. 65; Fig. 1.

### An RCC can provide error-corrective passive motion when its compliance parameters are chosen appropriately

**OBSERVATION:** The article presents an explanation of RCC action and guidelines for choosing RCC parameters; the support model includes lateral and angular springs, with their effective compliance center defined relative to the peg tip. [Abstract; Fig. 2, p. 65]

**AUTHOR INTERPRETATION:** RCC parameter choice can help avoid unsuccessful assembly by allowing contact forces to produce favorable relative motion during mating. [Abstract; Introduction, p. 65]

**INFERENCE:** The result supports passive error accommodation for the modeled insertion geometry; it does not establish universal success for arbitrary shapes, contact conditions, or robot structures.

**Intervention or measurement:** Design/analysis of lateral stiffness, angular stiffness, and compliance-center location in the spring-supported peg model.

**Observed result:** Guidelines are reported in the abstract. The accessible text does not supply the detailed parameter bounds or the experimental tests of each guideline.

**Causal strength:** UNCLEAR

**Controls:** Model fixes friction across contacts and removes gravity/inertia; the paper contrasts analytical planar parts with 3-D experimental parts.

**Alternative explanations not excluded:** Performance may depend on unmodeled contact mechanics, actual RCC construction, friction variability, and initial-error distributions.

**Scope limitations:** Conditions are derived with small-angle, quasi-static planar approximations and rigid parts.

**Source pointer:** Abstract; §1 Introduction, p. 65; Fig. 2.

## Important controls

- Constant and identical friction coefficient at every modeled contact.
- Small-angle approximation to obtain explicit solutions.
- Gravity and inertia explicitly ignored.
- Analytical system is planar; reported experiments use three-dimensional parts. [Introduction, p. 65]

## Critical assumptions

- Parts do not substantially deform relative to their compliant supports.
- Contact can be represented by the stated tab/slot geometry and Coulomb-like constant friction assumption.
- Quasi-static force equilibrium applies throughout relevant insertion stages.
- Initial positional/angular errors and support behavior remain in the model’s validity range.

## Limitations

Explicitly stated in the inspected introduction: planar round-peg/chamfered-hole model, flat tab/slot representation, constant identical friction, small-angle approximations, and omission of gravity and inertia. Detailed author-stated limitations elsewhere in the paper were not inspected.

## What this paper supports

For the specified quasi-static rigid-part model, contact geometry, support compliance, and friction enter calculable conditions for insertion forces and successful mating; the paper reports experimental verification of its insertion-force models.

## What this paper does not establish

It does not establish force-model validity for arbitrary 3-D geometries, nonconstant friction, deformable parts, dynamic insertion, gravity-dominated tasks, or all RCC designs. The accessible material does not establish quantitative accuracy, robustness, or replication.

## Explicit open questions

No explicit open questions were recovered from the inspected portions. The introduction identifies the practical need to accommodate placement/misalignment errors, but no formal future-work statement was inspected.

## Evidence concerns

**Replication:** No replication study or independent replication was identified in the inspected source material.

**Measurement limitations:** The abstract reports experimental verification, but apparatus, sensing, calibration, uncertainty, and quantitative data were not inspected.

**Potential confounding:** The extrapolation from planar, constant-friction theory to 3-D physical parts may be affected by unreported geometry/contact differences.

**Statistical / experimental concerns:** Sample size, repeats, error bars, and statistical analysis were not recovered; no statistical conclusion should be attributed to this paper card.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | [ASME PDF](https://asmedigitalcollection.asme.org/dynamicsystems/article-pdf/104/1/65/5777806/65_1.pdf), p. 65; [CiteSeerX text record](https://citeseerx.ist.psu.edu/document?doi=f4f7faf5480dd8645146eba58330439862ced921&repid=rep1&type=pdf) |
| Full paper | [ASME PDF](https://asmedigitalcollection.asme.org/dynamicsystems/article-pdf/104/1/65/5777806/65_1.pdf), pp. 65–77 (access denied in this run); [CiteSeerX record](https://citeseerx.ist.psu.edu/document?doi=f4f7faf5480dd8645146eba58330439862ced921&repid=rep1&type=pdf), partial text inspected |
| Main result | §1 Introduction, p. 65; Fig. 1 (assembly stages); abstract |
| Important control | §1 Introduction, p. 65 (constant friction, small angles, gravity/inertia ignored; 3-D experiments) |
| Limitations | §1 Introduction, p. 65 |
