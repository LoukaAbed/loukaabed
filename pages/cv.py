import streamlit as st
import utils.ui as ui

left, center, right =st.columns(3)
with center:
    st.title("Louka Abed")
st.markdown("Malden, MA 02148 | 617-942-1441 | [contact@loukaabed.com](mailto:contact@loukaabed.com)")
st.subheader("Clinical Data Scientist | AI Translational Medicine & Pharma R&D")
st.write("""International Medical Graduate (MD) combining clinical and biochemistry domain expertise with MS in Data Science and Mathematics foundations to validate, 
audit, model, and extract AI insights—accelerating novel drug discovery and building predictive translational medicine pipelines through a systems approach 
that integrates complex healthcare data streams, high-throughput genomic and proteomic registries, and heterogeneous multiomics architectures.""")

st.write("**Employment Status:** US Citizen | Fully authorized for US employment with no sponsorship required.")

st.divider()
st.markdown("### Education")
st.markdown("**MS in Data Science** | Eastern University | Expected Graduation: May 2027 (In Progress)")
st.write("""> **Coursework:** Principles of Python Programming, Data and Database Management with SQL.""")

st.markdown("**Bachelor of Medicine, Bachelor of Surgery (M.B. B.Ch.) (MD equivalent in the US) | Cairo University Faculty of Medicine **")
st.write("> **Clinical Clerkship** at Columbia University College of Physicians and Surgeons, New York. Routinely used Electronic Health Record (EHR). Passed US Medical Licensing Exam step 1 (USMLE step 1).")

st.markdown("**University of Massachusetts (UMass), Boston**")
st.write("* Bachelor of Science in Biochemistry & Mathematics Minor — *Summa Cum Laude graduate with Honors in Biochemistry, top of my class, GPA 3.86/4.00.*")

st.markdown("### Data Science Specialization & Technical Skills")
st.write("""
* **Core Programming:** Python, R, SQL.
* **Quantitative Coursework:** Calculus, linear algebra, differential equations, mathematical biology, probability & Statistics.
""")

st.divider()

st.markdown("### Systems, Data, & Computational Experience")

st.markdown("**Manufacturing Associate** | GMP Manufacturing - Moderna | Burlington, MA | 04/2023 – 03/2025")
st.write("""
* Working in the personalized cancer vaccine (PCV) unit.
* Routinely used enterprise software and databases: **SAP, Syncade, Sequencher**, SOP, GMP, aseptic technique, Biosafety Cabinet (BSC), chromatography.
""")

st.markdown("**Research Associate (Computational R&D)** | Columbia University Medical Center - Systems Biology | NY")
st.write("""
* **Predicting computationally cellular response (i.e., Gene Expression) to drug combinations (inspired by Connectivity Map).**
* Designed experiment, wrote protocol, ordered lab supplies & drugs, initiated cell culture, propagated, maintained & cryopreserved stock of mammalian immortal cells (MCF7), cell counting, aseptic/sterile technique.
* In vitro drug testing, determined the optimum drug dosage for maximum mRNA cellular response, isolation & quantification mRNA via spectrophotometry, sent mRNA for gene sequencing.
""")

st.markdown("**Medical Data Analyst** | Innodata – Synodex Division | Hackensack, NJ")
st.write("""
* Literature review to create up-to-date evidence-based medical risk elements in order to **accurately predict the real liability in disability & life insurance**.
* **Advanced skills in Excel:** VB macros, searching, sorting, matching, text extraction/editing datasets.
""")

st.divider()

st.markdown("### Clinical Operations & Medical Registries")

st.markdown("**Family Medicine Resident Physician** | Ministry of Health | Port Said, Egypt | 03/2021 – 02/2023")
st.write("""
* Rotation through primary care clinic, pediatrics, internal Medicine, and emergency medicine. **Utilized Electronic Health Record (EHR) databases natively.**
""")

st.markdown("**Medical Internship** | Cairo University Teaching Hospitals | Cairo, Egypt | 03/2019 – 04/2020")
st.write("""
* One year of clinical clerkships required to be a licensed physician in Egypt.
""")

st.divider()

st.markdown("### Laboratory Research Foundations")

st.markdown("**Research Associate (Summer)** | Columbia University Medical Center, Nephrology Division | NY")
st.write("* Role of Copy-Number Variations (CNVs) in children. Used Real-Time qPCR (qRT-PCR) to validate & quantify rare CNVs. Used online data resources extensively: **UCSC genome browser, dbSNP**, Primer3, primer design.")

st.markdown("**Process Development Associate (Contract)** | Broad Institute | Cambridge, MA")
st.write("* Sequencing genomes using Primer Walking. **Operating Multiprobe robot for automatic liquid reagents dispensing (High Throughput Technique)**, 96-wells, barcode plate readers, thermal plate sealers.")

st.markdown("**Research Assistant (Summer)** | Beth Israel Deaconess Medical Center - Matrix Biology | Boston, MA")
st.write("* Carcinoma-associated fibroblasts study. Skills in tissue genotyping, tumor cell culture (4T1), primary culture, embedding, microtome sectioning, IHC & IF staining, H&E staining.")

st.markdown("**Research Assistant (Work-study)** | University of Massachusetts, Department of Biology | Boston, MA")
st.write("* Cell signaling study in-vivo Drosophila using RNAi vectors. DNA cloning/subcloning, restriction enzymes, ligation, competent E. Coli, transformations, agar plating, PCR screening, minipreps, spectrophotometry.")

st.divider()

st.markdown("**Accomplishments & Awards:**")
st.write("• Emil Fischer Book Award, Honors, and Distinction in Biochemistry • Dean's List • Tutor Certificate of Recognition • Classroom Leadership Award • Ronald E. McNair Scholar")

st.markdown("**Certifications:**")
st.write("• Certified General Medical Practitioner (Physician/MD) in Egypt • Certified in Immediate Life Support (ILS) / Basic Life Support (BLS) (European Resuscitation Council)")

st.divider()

st.markdown("### Publications")
st.write('Phillip Kyriakakis; Marla Tipping; ***Louka Abed**; Alexey Veraksa. "Tandem affinity purification in Drosophila: The advantages of the GS-TAP system." *Fly* Vol: 2:229-235. **(*Published under former name*)**')

st.divider()

ui.message()