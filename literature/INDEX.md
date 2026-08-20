# Literature Index

**Status:** DISCOVERY_COMPLETE

**Topic:** Mechanistic understanding of robust contact-rich robotic assembly under physical and perceptual uncertainty.

**Discovery date:** 2026-08-20

**Literature cutoff / search date:** 2026-08-20

**Broad query scope:** Contact-rich robotic assembly; peg/hole and tight-clearance insertion; quasi-static contact mechanics; compliance, hybrid/impedance control; force/tactile/vision sensing and contact-state inference; learned policies; sim-to-real; evaluation and failure recovery.

## Coverage assessment

Provisional map covers rigid-part mechanics and passive compliance; hybrid/impedance control; search and wrench-based state inference; sensor-minimal compliance; learned force/tactile policies; vision–touch staging/fusion; contact simulation and transfer; and evaluation/fault monitoring. The first pass found an apparent regime distinction: passive or active compliance can suffice in engineered settings, whereas sensing improves difficult, tight-tolerance, occluded, or variable-orientation cases. It also found that explicit inference and recurrent/RL policies have rarely been compared under matched uncertainty, safety, and time constraints.

Targeted challenge added uncertainty-aware contact/action planning as a ninth explanatory family: robustness can be designed into action selection and physical task structure before reactive control or learned recovery. It also split terminal success from phase-resolved, off-nominal diagnosis and recovery. No direct replication failure of a flagship control or tactile-policy result was found. The strongest contradiction is methodological: binary success metrics can conceal characteristic alignment, engagement, and recovery failures. Coverage is saturated for material omissions; further searching is unlikely to change the map beyond more planning papers or benchmarks.

## Discovery records

| Classification | Paper | Year / status | Source URL | Evidence role | Relevance | Card path |
|---|---|---|---|---|---|---|
| CORE | Whitney, *Quasi-Static Assembly of Compliantly Supported Rigid Parts* | 1982, published, JDSMC | https://doi.org/10.1115/1.3149634 | Mechanics / passive compliance | Jamming, clearance, misalignment, RCC | literature/cards/whitney_1982.md |
| CORE | Raibert & Craig, *Hybrid Position/Force Control of Manipulators* | 1981, published, JDSMC | https://doi.org/10.1115/1.3139652 | Active-contact control | Classical force/position account | |
| CORE | Hogan, *Impedance Control: Part I—Theory* | 1985, published, JDSMC | https://doi.org/10.1115/1.3140702 | Interaction-dynamics theory | Compliance/admittance basis | |
| CORE | Chhatpar & Branicky, *Search Strategies for Peg-in-Hole Assemblies with Position Uncertainty* | 2001, published, IROS | https://doi.org/10.1109/IROS.2001.977187 | Search/localization | Contact probes under pose uncertainty | |
| CORE | Chhatpar & Branicky, *Localization for Robotic Assemblies with Position Uncertainty* | 2003, published, IROS | https://citeseerx.ist.psu.edu/document?doi=3dd9b81f0c854367b2d861b4604e249e3d7545b2&repid=rep1&type=pdf | Physical perception | Contact-configuration localization | literature/cards/chhatpar_branicky_2003.md |
| CORE | Jasim, Plapper & Voos, *Position Identification in Force-Guided Robotic Peg-in-Hole Assembly Tasks* | 2014, published, Procedia CIRP | https://doi.org/10.1016/j.procir.2014.10.077 | Force-based state estimation | Wrench-only geometric identification | |
| CORE | Park et al., *Compliance-Based Robotic Peg-in-Hole Assembly Strategy Without Force Feedback* | 2017, published, IEEE TIE | https://doi.org/10.1109/TIE.2017.2682002 | Sensor-minimal competing mechanism | Compliance without F/T sensing | literature/cards/park_2017.md |
| CORE | Inoue et al., *Deep Reinforcement Learning for High Precision Assembly Tasks* | 2017, published, IROS | https://arxiv.org/abs/1708.04033 | Learned-policy alternative | Recurrent policy under pose error | literature/cards/inoue_2017.md |
| CORE | Triyonoputro, Wan & Harada, *Quickly Inserting Pegs into Uncertain Holes* | 2019, published, IROS | https://doi.org/10.1109/IROS40897.2019.8968072 | Multimodal system | Vision, search, impedance, F/T staging | |
| CORE | Dong et al., *Tactile-RL for Insertion* | 2021, published, ICRA | https://doi.org/10.1109/ICRA48506.2021.9561646 | Comparative tactile-learning evidence | Modality and geometry generalization | literature/cards/dong_2021.md |
| CORE | Gibbons, Albini & Maiolino, *A Tactile Feedback Insertion Strategy for Peg-in-Hole Tasks* | 2023, published, ICRA | https://doi.org/10.1109/ICRA48891.2023.10160879 | Tactile capability | Real fine-clearance insertion | |
| SUPPORTING | Narang et al., *Factory: Fast Contact for Robotic Assembly* | 2022, published, RSS | https://www.roboticsproceedings.org/rss18/p035.pdf | Simulation capability | Contact-model fidelity context | |
| CORE | Tang et al., *IndustReal* | 2023, preprint; venue needs verification | https://arxiv.org/abs/2305.17110 | Sim-to-real mechanism | Transfer under model discrepancy | literature/cards/tang_2023.md |
| SUPPORTING | *Towards Generalized Robot Assembly through Compliance-Enabled Contact Formations* | 2023, preprint; metadata needs verification | https://arxiv.org/abs/2303.05565 | Contact-formation abstraction | Transferable compliant contacts | |
| CORE | Jha et al., *Imitation and Supervised Learning of Compliance for Robotic Assembly* | 2021, preprint; venue needs verification | https://arxiv.org/abs/2111.10488 | Learned compliance/inference | Contact exploration and misalignment inference | |
| CORE | Lenz et al., *Analysing the Interplay of Vision and Touch for Dexterous Insertion Tasks* | 2024, published, CoRL | https://openreview.net/pdf?id=93UzkM03Vi | Comparative modality evidence | Vision/touch under tight tolerances | literature/cards/lenz_2024.md |
| CORE | Cao & Xiao, *On Efficient and Flexible Autonomous Robotic Insertion Assembly in the Presence of Uncertainty* | 2024, published, RA-L | https://doi.org/10.1109/LRA.2024.3404749 | Explicit uncertainty / physical inference | Complex tight-clearance assembly | |
| SUPPORTING | Jiang et al., *A Review of Robotic Assembly Strategies for the Full Operation Procedure* | 2023, published, RCIM | https://doi.org/10.1016/j.rcim.2022.102366 | Field-map scaffold | Evaluation and fault-monitoring taxonomy | |
| SUPPORTING | Suomalainen, Karayiannidis & Kyrki, *A Survey of Robot Manipulation in Contact* | 2022, published, RAS | https://doi.org/10.1016/j.robot.2022.104224 | Field-map scaffold | Contact-manipulation taxonomy | |
| CORE | Wirnshofer et al., *Robust, Compliant Assembly via Optimal Belief Space Planning* | 2018, published, ICRA | https://doi.org/10.1109/ICRA.2018.8460995 | Uncertainty-aware planning | Action selection with pose/contact uncertainty | literature/cards/wirnshofer_2018.md |
| SUPPORTING | Rosell, Basañez & Suárez, *Compliant-Motion Planning and Execution for Robotic Assembly* | 1999, published, ICRA | https://doi.org/10.1109/ROBOT.1999.774017 | Contact-space planning | Geometry-specified, planar scope boundary | |
| PERIPHERAL | Ofori-Ampofo, Kahou & Thekinen, *REBOOT: From Failure to Recovery* | 2026, preprint/dataset; metadata needs verification | https://nanayawoa.github.io/REBOOT/ | Recovery benchmark | Phase-resolved off-nominal evaluation | |
| PERIPHERAL | Ma et al., *WorkBenchMark — A LEGO-Based Assembly Benchmark* | 2026, benchmark; proceedings need verification | https://workbenchmark.github.io/ | System-level scope boundary | Multi-part sequencing and symbolic/physical constraints | |

Metadata caveats: archival status for IndustReal and Jha et al., and authorship/venue for the contact-formations preprint, require verification if selected.
