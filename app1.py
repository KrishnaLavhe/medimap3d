import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediMap 3D",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500&family=Space+Mono:wght@400;700&display=swap');

/* ---- Root palette ---- */
:root {
    --off-white:  #F5F4F0;
    --teal-light: #A8D5D1;
    --teal-mid:   #5BADA6;
    --teal-dark:  #2E7D78;
    --ink:        #1C2B2A;
    --ink-soft:   #3E5250;
    --line:       #C9E0DE;
    --card-bg:    #FFFFFF;
    --accent:     #D4F0ED;
}

/* ---- Body / App shell ---- */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--off-white) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

[data-testid="stHeader"] { background: transparent !important; }

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #E8F6F5 0%, #F5F4F0 100%) !important;
    border-right: 1.5px solid var(--line) !important;
}
[data-testid="stSidebar"] * { color: var(--ink-soft) !important; }
[data-testid="stSidebarNavItems"] { padding-top: 0.5rem; }

/* ---- Hide default Streamlit chrome ---- */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; }

/* ---- Typography helpers ---- */
.display-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.6rem, 5vw, 4rem);
    font-weight: 700;
    color: var(--teal-dark);
    letter-spacing: -0.5px;
    line-height: 1.15;
    margin-bottom: 0.15rem;
}
.display-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--teal-mid);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.6rem;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.95rem;
    font-weight: 600;
    color: var(--teal-dark);
    border-bottom: 2px solid var(--teal-light);
    padding-bottom: 0.35rem;
    margin-bottom: 1rem;
}
.body-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.02rem;
    line-height: 1.82;
    color: var(--ink-soft);
}
.lead-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.12rem;
    font-weight: 500;
    line-height: 1.75;
    color: var(--ink);
}

/* ---- Cards ---- */
.card {
    background: var(--card-bg);
    border: 1.5px solid var(--line);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 12px rgba(46,125,120,0.05);
}
.card-teal {
    background: linear-gradient(135deg, #E6F7F6 0%, #FAFCFC 100%);
    border-left: 4px solid var(--teal-mid);
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}
.pill {
    display: inline-block;
    background: var(--accent);
    color: var(--teal-dark);
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 0.25rem 0.75rem;
    border-radius: 50px;
    margin-right: 0.4rem;
    margin-bottom: 0.4rem;
    border: 1px solid var(--teal-light);
}
.divider {
    border: none;
    border-top: 1.5px solid var(--line);
    margin: 1.8rem 0;
}
.highlight-box {
    background: linear-gradient(135deg, var(--teal-dark), var(--teal-mid));
    color: white;
    border-radius: 12px;
    padding: 1.4rem 1.8rem;
    margin: 1.2rem 0;
}
.highlight-box p { color: white !important; margin: 0; font-size: 1.05rem; line-height: 1.7; }
.tag-mono {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--teal-mid);
    background: var(--accent);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
}
.step-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--teal-light);
    line-height: 1;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1rem 0 0.5rem 0;'>
        <div style='font-family: Cormorant Garamond, serif; font-size: 1.5rem; font-weight: 700; color: #2E7D78;'>🧠 MediMap 3D</div>
        <div style='font-family: Space Mono, monospace; font-size: 0.62rem; letter-spacing: 2px; color: #5BADA6; text-transform: uppercase; margin-top: 2px;'>Real-Time 3D MRI Pathology</div>
    </div>
    <hr style='border-color: #C9E0DE; margin: 0.8rem 0 1.2rem 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  Overview & Abstract", "📖  Introduction", "⚙️  System Overview", "🔭  Future Scope", "🌍  Social Impact"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr style='border-color: #C9E0DE; margin: 1.5rem 0 1rem 0;'>
    <div style='font-family: DM Sans, sans-serif; font-size: 0.78rem; color: #5BADA6; line-height: 1.6;'>
        <b>Stack</b><br>
        Unity · FastAPI · MONAI · nnU-Net<br>
        <br>
        <b>Domain</b><br>
        Medical Imaging · AI · 3D Rendering
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE 1 – OVERVIEW & ABSTRACT
# ─────────────────────────────────────────────────────────────────────────────
if page == "🏠  Overview & Abstract":

    st.markdown('<div class="display-title">MediMap 3D</div>', unsafe_allow_html=True)
    st.markdown('<div class="display-sub">Real-Time 3D MRI Pathological Visualization · Unity Volume Rendering</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="pill">Medical AI</div>
    <div class="pill">3D Segmentation</div>
    <div class="pill">nnU-Net</div>
    <div class="pill">MONAI</div>
    <div class="pill">Unity</div>
    <div class="pill">FastAPI</div>
    <br>
    """, unsafe_allow_html=True)

    # Abstract card
    st.markdown('<div class="section-title">Abstract</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="lead-text">
            MediMap 3D is an end-to-end, real-time medical visualization platform that transforms conventional 
            grayscale MRI data into interactive, AI-annotated three-dimensional anatomical maps — giving clinicians 
            a precise, navigable view of pathological tissue without the cognitive burden of manual 2D slice interpretation.
        </p>
        <hr class="divider" style="margin: 1rem 0;">
        <p class="body-text">
            The system integrates a Unity-based volumetric rendering front-end with a Python-powered deep learning 
            inference backend. DICOM image stacks are compressed in-memory and transmitted via a FastAPI endpoint, 
            where the MONAI framework normalizes and reconstructs them into a full 3D tensor. An nnU-Net segmentation 
            model then performs voxel-level inference, producing a probability heatmap that quantifies the likelihood 
            of pathological tissue at every point in the volume — from 0.0 (healthy) to 1.0 (pathological).
        </p>
        <p class="body-text">
            This heatmap is returned to Unity as a raw binary float32 array, reconstructed as a Texture3D, and 
            injected directly into a custom ray-marching shader. The result is a glowing, interactive overlay 
            superimposed on the patient's own anatomy — a "GPS for Surgeons" that pinpoints tumor boundaries, 
            assists surgical planning, and can be operated on commodity hardware in regional clinical settings.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tap-to-explore cards
    st.markdown('<div class="section-title">Explore the Project</div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text" style="margin-bottom:1.2rem;">Tap any section in the sidebar to dive deeper into the project.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-teal">
            <div style='font-family: Space Mono, monospace; font-size:0.65rem; color:#5BADA6; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.5rem;'>📖 Introduction</div>
            <div style='font-family: Cormorant Garamond, serif; font-size:1.2rem; font-weight:600; color:#1C2B2A; margin-bottom:0.4rem;'>The Problem We Solve</div>
            <p class='body-text' style='font-size:0.9rem;'>Why traditional 2D MRI viewing is cognitively demanding and how MediMap 3D removes that burden.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card-teal">
            <div style='font-family: Space Mono, monospace; font-size:0.65rem; color:#5BADA6; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.5rem;'>🔭 Future Scope</div>
            <div style='font-family: Cormorant Garamond, serif; font-size:1.2rem; font-weight:600; color:#1C2B2A; margin-bottom:0.4rem;'>Where This Is Headed</div>
            <p class='body-text' style='font-size:0.9rem;'>Multi-organ expansion, hospital integration, and an autonomous body-part classifier — the roadmap ahead.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card-teal">
            <div style='font-family: Space Mono, monospace; font-size:0.65rem; color:#5BADA6; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.5rem;'>⚙️ System Overview</div>
            <div style='font-family: Cormorant Garamond, serif; font-size:1.2rem; font-weight:600; color:#1C2B2A; margin-bottom:0.4rem;'>How It Works</div>
            <p class='body-text' style='font-size:0.9rem;'>The full data flow from DICOM upload through AI inference to the 3D heatmap overlay — no code, just clarity.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card-teal">
            <div style='font-family: Space Mono, monospace; font-size:0.65rem; color:#5BADA6; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.5rem;'>🌍 Social Impact</div>
            <div style='font-family: Cormorant Garamond, serif; font-size:1.2rem; font-weight:600; color:#1C2B2A; margin-bottom:0.4rem;'>Lives Changed</div>
            <p class='body-text' style='font-size:0.9rem;'>Democratizing diagnostic-grade imaging for underserved clinics and communities worldwide.</p>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE 2 – INTRODUCTION
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📖  Introduction":

    st.markdown('<div class="display-sub">Project Context</div>', unsafe_allow_html=True)
    st.markdown('<div class="display-title">Introduction</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">The Diagnostic Challenge</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="lead-text">
            Every day, radiologists and surgeons face a formidable cognitive task: reconstructing a three-dimensional 
            reality from a sequence of flat, two-dimensional grayscale images.
        </p>
        <p class="body-text">
            Magnetic Resonance Imaging (MRI) remains one of the most powerful tools in modern medicine for visualizing 
            soft tissue structures — the brain, spinal cord, organs, and the tumors that grow within them. Yet despite 
            this diagnostic power, the conventional way of reading MRI data has changed little in decades. A clinician 
            scrolls through dozens or even hundreds of sequential slices, building a mental model of the patient's 
            three-dimensional anatomy slice by slice. This demands exceptional spatial reasoning, years of training, 
            and sustained concentration — often under the pressure of high patient volumes and time constraints.
        </p>
        <p class="body-text">
            The consequences of this cognitive burden are significant. Subtle tumors nestled near critical vascular 
            or functional structures can be missed or misjudged. Spatial relationships — "Is this mass compressing 
            the optic nerve? How close is it to the motor cortex?" — are difficult to appreciate on a flat screen. 
            Pre-surgical planning suffers when a surgeon cannot easily visualize tumor depth or margins relative to 
            the surrounding healthy anatomy.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">The Existing Landscape</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            Three-dimensional medical imaging software does exist, but it comes with barriers that limit its reach. 
            Enterprise-grade volumetric visualization platforms are expensive, often requiring dedicated workstations 
            or proprietary hardware, specialized IT infrastructure, and licensing costs that place them out of reach 
            for smaller regional hospitals and clinics — exactly the settings where diagnostic support is needed most.
        </p>
        <p class="body-text">
            AI-powered diagnostic tools are also emerging, but they tend to operate as "black boxes" — producing 
            a report or classification score without giving the clinician an intuitive, interactive visual anchor. 
            A probability score on a page does not tell a surgeon where to cut.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">MediMap 3D — The Response</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-box">
        <p>
            MediMap 3D was conceived to close the gap between powerful AI inference and practical clinical usability. 
            The goal is not simply to detect pathology, but to show it — spatially, interactively, and with 
            calibrated confidence — directly inside the patient's own anatomical volume.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p class="body-text">
            Think of it as a GPS for surgeons. Just as a navigation system overlays your precise route onto a 
            real map of the roads ahead, MediMap 3D overlays an AI-generated probability heatmap directly 
            onto the patient's three-dimensional MRI volume. The radiologist or surgeon does not need to mentally 
            reconstruct where the tumor is — they can see it, rotate it, slice into it, and adjust the confidence 
            threshold in real time.
        </p>
        <p class="body-text">
            The platform is built on accessible, open technologies: Unity for interactive 3D rendering, FastAPI 
            for the backend server, and MONAI with nnU-Net for medical-grade deep learning segmentation. It is 
            designed to run on a standard PC with an internet connection — no proprietary hardware, no 
            prohibitive licensing fees.
        </p>
        <p class="body-text">
            MediMap 3D represents a shift in how AI diagnostic tools should be designed: not as isolated 
            classifiers, but as interactive visual collaborators that augment and support the clinician's 
            own expertise.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE 3 – SYSTEM OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────
elif page == "⚙️  System Overview":

    st.markdown('<div class="display-sub">Architecture</div>', unsafe_allow_html=True)
    st.markdown('<div class="display-title">System Overview</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p class="lead-text">
        MediMap 3D operates as a tightly integrated client–server pipeline. The Unity front-end handles all 
        user interaction and 3D rendering, while the Python backend handles all heavy computation. Data flows 
        efficiently between the two in compressed binary form, keeping latency low and memory usage lean.
    </p>
    """, unsafe_allow_html=True)

    # Step 1
    st.markdown('<div class="section-title">Stage 1 — DICOM Ingestion & Upload</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.markdown('<div class="step-num">01</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <p class="body-text">
                The clinical workflow begins inside Unity, where the radiologist or technician uses a file browser 
                to select the patient's DICOM folder. DICOM (Digital Imaging and Communications in Medicine) is the 
                universal standard format for medical imaging data — each file encodes one slice of the MRI scan 
                along with rich metadata including scanner parameters, patient identifiers, and imaging protocol.
            </p>
            <p class="body-text">
                Rather than uploading each slice individually — which would be slow and order-sensitive — MediMap 3D 
                bundles all the DICOM files into a single Zip archive entirely in RAM, without ever writing to disk. 
                This in-memory compression preserves the correct spatial ordering of slices and significantly reduces 
                the data size before transmission. The compressed archive is then sent to the backend server via a 
                single HTTP request, keeping the upload fast and atomic.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Step 2
    st.markdown('<div class="section-title">Stage 2 — Server-Side Inference</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.markdown('<div class="step-num">02</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <p class="body-text">
                The FastAPI backend receives the zip stream, unpacks it into a temporary memory buffer, and 
                immediately validates the DICOM headers to confirm that the data is well-formed and contains the 
                expected imaging parameters.
            </p>
            <p class="body-text">
                The individual 2D slices are then stacked by the MONAI medical imaging framework into a unified 
                three-dimensional tensor — a volumetric representation of the entire organ where every voxel occupies 
                a precise position in three-dimensional space. MONAI also applies standardization transforms to 
                normalize Hounsfield Unit (HU) intensity values, ensuring that the AI model performs consistently 
                regardless of the MRI scanner manufacturer or acquisition protocol used.
            </p>
            <p class="body-text">
                This 3D volume is passed to an nnU-Net segmentation model — the current gold standard for volumetric 
                medical image segmentation. nnU-Net performs full-volume inference, meaning it sees the entire organ 
                at once rather than processing isolated patches. This holistic view allows the model to capture 
                long-range spatial context, accurately delineate tumor boundaries, and distinguish irregular masses 
                from surrounding healthy tissue. The output is a probability map of identical dimensions to the 
                input volume, where each voxel carries a value between 0.0 (confidently healthy) and 1.0 
                (confidently pathological).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Step 3
    st.markdown('<div class="section-title">Stage 3 — 3D Heatmap Transmission & Rendering</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.markdown('<div class="step-num">03</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <p class="body-text">
                The 3D probability map is flattened into a compact raw float32 binary array and returned to the 
                Unity client over the same HTTP connection. This binary format is far more compact than JSON or XML 
                and requires no parsing overhead — it maps directly onto memory.
            </p>
            <p class="body-text">
                Inside Unity, a C# script reconstructs this binary stream into a Texture3D object — a three-dimensional 
                texture that mirrors the exact spatial dimensions of the original MRI volume. This texture is injected 
                as a secondary data source into the Unity Volume Rendering package's ray-marching shader, running 
                alongside the patient's base anatomical volume.
            </p>
            <p class="body-text">
                The shader samples both the anatomical MRI texture and the AI probability texture simultaneously at 
                every point along each ray of light cast through the volume. Where the AI probability exceeds a 
                user-defined threshold, the shader adds a vivid glowing red emission to those voxels — painting 
                pathological tissue in a visually distinct color without obscuring the surrounding anatomy. The 
                result is a fully interactive 3D brain (or organ) with the tumor lit up from within.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Step 4 — UX controls
    st.markdown('<div class="section-title">Stage 4 — Doctor Dashboard & Controls</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.markdown('<div class="step-num">04</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <p class="body-text">
                The clinical user interface is designed for intuitive, real-time interaction. A Confidence Slider 
                allows the clinician to dynamically adjust the probability threshold at which tissue is highlighted — 
                for example, setting it to 90% certainty shows only the most definitively pathological regions, 
                while lowering it reveals borderline areas that warrant additional scrutiny.
            </p>
            <p class="body-text">
                A set of diagnostic presets allows instant switching between optimized viewing modes: Bone mode, 
                Soft Tissue mode, and Tumor-Focused mode — each tuning the volume rendering transfer function to 
                make the most clinically relevant structures visible. A virtual slicing tool allows the clinician 
                to "cut" into the 3D volume along any plane, revealing the tumor's depth and its spatial relationship 
                to critical adjacent structures.
            </p>
            <p class="body-text">
                All slider adjustments update the 3D render in real time with no lag, giving the clinician a 
                genuinely interactive exploratory experience rather than a static snapshot.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE 4 – FUTURE SCOPE
# ─────────────────────────────────────────────────────────────────────────────
elif page == "🔭  Future Scope":

    st.markdown('<div class="display-sub">Roadmap</div>', unsafe_allow_html=True)
    st.markdown('<div class="display-title">Future Scope</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p class="lead-text">
        MediMap 3D's current implementation focuses on neurological pathology — but the architecture is 
        explicitly designed to grow. The pipeline is organ-agnostic by nature: any volumetric imaging data 
        paired with a trained segmentation model can flow through the same system. What follows is the 
        trajectory we envision.
    </p>
    """, unsafe_allow_html=True)

    # Multi-organ
    st.markdown('<div class="section-title">Multi-Organ Expansion</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            The most immediate extension of MediMap 3D is broadening its diagnostic reach beyond the brain 
            to cover the full spectrum of oncological imaging. The same data pipeline — DICOM ingestion, 
            MONAI normalization, nnU-Net segmentation, Unity heatmap rendering — applies directly to other 
            organs with only a change of the trained model weights and transfer function presets.
        </p>
        <p class="body-text">
            Planned future modules include:
        </p>
        <div style='margin: 0.8rem 0 0.5rem 0;'>
            <span class='pill'>🫁 Lungs</span>
            <span class='pill'>🩺 Prostate</span>
            <span class='pill'>🫀 Liver</span>
            <span class='pill'>🩹 Kidney</span>
            <span class='pill'>🦴 Spine</span>
            <span class='pill'>🔬 Pancreas</span>
        </div>
        <p class="body-text">
            For lung imaging, the system would detect and localize nodules against the textured background of 
            bronchial and vascular structures — where 3D context is especially critical for staging. For prostate 
            cancer, volumetric MRI segmentation allows precise Gleason-grade estimation that 2D reading struggles 
            to provide. Each organ module would ship with disease-specific presets, ensuring that the rendering 
            parameters are tuned for what clinicians actually need to see.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Autonomous classifier
    st.markdown('<div class="section-title">Autonomous Body-Part Classifier</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-box">
        <p>
            In any real clinical workflow, human error is inevitable. A radiologist selecting the wrong organ type 
            from a dropdown — labelling a chest CT as a brain scan — would feed the wrong segmentation model and 
            produce meaningless results. MediMap 3D's roadmap includes an intelligent pre-processing classifier 
            that removes this risk entirely.
        </p>
    </div>
    <div class="card">
        <p class="body-text">
            Before the DICOM stack is passed to any segmentation model, a lightweight convolutional neural network 
            will analyse the volume's DICOM metadata and a sample of axial slices to automatically determine which 
            anatomical region is present. If the system detects that it is looking at a chest CT — regardless of 
            what option the radiologist selected in the UI — it will automatically route the data to the correct 
            lung segmentation model, alert the clinician of the mismatch, and proceed with the appropriate inference.
        </p>
        <p class="body-text">
            This self-correcting behavior dramatically reduces the chance of diagnostic error stemming from 
            workflow mistakes, and makes the system more robust for deployment in busy, high-throughput 
            environments where attention lapses are a reality rather than an exception. The classifier adds 
            a layer of intelligence upstream of the segmentation pipeline — not just answering "where is the tumor" 
            but first establishing "what are we even looking at?"
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Hospital integration
    st.markdown('<div class="section-title">Hospital & PACS Integration</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            The next major milestone beyond standalone deployment is deep integration with hospital information 
            systems. Modern hospitals manage imaging data through Picture Archiving and Communication Systems 
            (PACS) — centralized servers that store, retrieve, and distribute DICOM studies across the institution. 
            A future version of MediMap 3D will connect directly to hospital PACS via the DICOM network protocol, 
            allowing scans to be pulled directly from the archive without any manual file selection by the user.
        </p>
        <p class="body-text">
            Integration with Electronic Health Record (EHR) systems would allow the AI-generated probability maps 
            and confidence reports to be automatically attached to the patient's record, creating an auditable 
            chain of AI-assisted findings that can be reviewed, overridden, or validated by the attending radiologist. 
            Role-based access controls would ensure that the right level of interaction is available to radiologists, 
            surgeons, and referring physicians respectively.
        </p>
        <p class="body-text">
            Cloud deployment via containerized microservices (Docker, Kubernetes) would allow hospital IT teams 
            to deploy the inference backend on existing cloud infrastructure, scaling compute resources dynamically 
            with imaging volume — from a quiet rural clinic processing a handful of scans per day to a major 
            university hospital with continuous throughput.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quantitative reporting
    st.markdown('<div class="section-title">Quantitative Reporting & Longitudinal Tracking</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            Beyond visualization, future versions will generate structured quantitative reports: tumor volume in 
            cubic centimetres, centroid coordinates in patient space, surface area estimates, and proximity 
            measurements to named anatomical landmarks. These metrics, reproducibly computed from AI segmentation, 
            would support objective longitudinal tracking — comparing a patient's scan from three months ago to 
            today's scan with pixel-perfect precision to assess treatment response or disease progression.
        </p>
        <p class="body-text">
            Combined with the 3D render, this transforms MediMap 3D from a visualization aid into a 
            quantitative diagnostic instrument — one capable of supporting clinical trials, treatment response 
            assessment, and outcomes research at scale.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE 5 – SOCIAL IMPACT
# ─────────────────────────────────────────────────────────────────────────────
elif page == "🌍  Social Impact":

    st.markdown('<div class="display-sub">Purpose</div>', unsafe_allow_html=True)
    st.markdown('<div class="display-title">Social Impact</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p class="lead-text">
        Technology in medicine has always carried a question beyond "does it work?" — the more important 
        question is "who does it reach?" MediMap 3D was built with that question at its centre.
    </p>
    """, unsafe_allow_html=True)

    # Democratizing access
    st.markdown('<div class="section-title">Democratizing Diagnostic Quality</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            Advanced 3D medical imaging tools have historically been the privilege of well-resourced academic 
            medical centres — hospitals in major cities with the budget for expensive enterprise software, 
            dedicated high-performance workstations, and specialist radiology teams. For regional hospitals, 
            rural health centres, and clinics serving lower-income populations, these tools are simply inaccessible.
        </p>
        <p class="body-text">
            MediMap 3D is designed from the ground up to run on a standard consumer-grade PC with an 
            internet connection — no proprietary hardware, no six-figure licensing contracts. The backend 
            inference can be hosted on affordable cloud infrastructure and shared across multiple facilities 
            simultaneously. This means that a clinic in a small town or a hospital in a low-resource region 
            can access diagnostic-grade AI pathology visualization that was previously available only to 
            the largest institutions. The gap between tier-one and tier-three healthcare facilities narrows 
            meaningfully when the tool fits in a browser upload and runs on commodity hardware.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Reducing human error
    st.markdown('<div class="section-title">Reducing Diagnostic Error</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-box">
        <p>
            Diagnostic error in radiology is not a failure of skill — it is a predictable consequence of 
            asking the human visual system to do something it was not optimized for: reconstructing 
            three-dimensional spatial relationships from two-dimensional sequences under time pressure. 
            MediMap 3D reduces this structural vulnerability.
        </p>
    </div>
    <div class="card">
        <p class="body-text">
            By providing an interactive 3D heatmap that highlights regions of pathological probability, the 
            system acts as a second pair of eyes — one that has reviewed thousands of scans and does not 
            fatigue. It does not replace the radiologist's judgment; it supports it. Clinicians can validate 
            the AI's findings, adjust confidence thresholds to explore borderline regions, and override 
            the system's assessment. The result is a human-AI collaboration that combines the contextual 
            reasoning of an experienced clinician with the pattern-recognition precision of a trained 
            deep learning model.
        </p>
        <p class="body-text">
            Earlier detection of tumors — particularly small masses in early-stage disease — dramatically 
            changes patient outcomes. Survival rates for most cancers correlate strongly with the stage at 
            which they are detected. A tool that makes early-stage tumors more visible to more clinicians, 
            in more hospitals, is not just a technological achievement — it is a measurable contribution 
            to lives saved.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Surgical planning
    st.markdown('<div class="section-title">Empowering Surgeons & Surgical Planning</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            For neurosurgeons and oncological surgeons, the quality of pre-operative planning is directly 
            tied to patient safety during the procedure. Knowing the precise three-dimensional boundaries 
            of a tumor — how close it is to the motor cortex, whether it wraps around a major vessel, how 
            deep below the surface it sits — allows a surgeon to plan the safest possible approach, 
            minimizing the risk of damaging healthy tissue and maximizing the likelihood of complete resection.
        </p>
        <p class="body-text">
            The MediMap 3D slicing tool and interactive rotation give surgeons a way to mentally rehearse 
            the procedure before making a single incision. This kind of interactive pre-surgical visualization 
            has been shown in clinical literature to reduce operative time, improve resection completeness, 
            and lower complication rates. Making it available as an affordable, interactive tool rather than 
            a proprietary pre-operative simulation suite extends this benefit to far more surgical teams.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Education
    st.markdown('<div class="section-title">Medical Education & Training</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p class="body-text">
            The interactive 3D environment created by MediMap 3D also has significant value as an 
            educational tool. Medical students and radiology residents learning to interpret MRI data 
            currently rely on textbooks, static 3D atlases, and the guidance of senior clinicians. 
            MediMap 3D provides a dynamic alternative: real patient volumes with AI annotations that 
            students can explore, rotate, threshold, and interrogate.
        </p>
        <p class="body-text">
            Training institutions with limited access to rare pathology cases can use an AI-annotated 
            library of 3D volumes to expose students to a far wider range of presentations than any 
            single hospital could encounter organically. This shortens the learning curve for pattern 
            recognition, builds spatial reasoning skills faster, and ultimately produces more 
            diagnostically capable clinicians.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Summary statement
    st.markdown("""
    <div class="highlight-box" style="margin-top: 1.5rem;">
        <p style="font-family: Cormorant Garamond, serif; font-size: 1.3rem; font-weight: 600;">
            MediMap 3D is not just a visualization tool. It is an argument that the highest standard 
            of diagnostic support should not be a privilege — it should be a baseline, available wherever 
            a patient needs it.
        </p>
    </div>
    """, unsafe_allow_html=True)
