import img1 from "../471203311_8904761216271834_497589100867517360_n.jpg";
import img2 from "../556881529_948973237506176_8927324503498204558_n.jpg";
import img3 from "../557592656_2167659063639691_1438200609746433144_n.jpg";
import img4 from "../644513092_796806493442113_2973354065220771693_n.jpg";
import img5 from "../81176266_191037628733039_2649829955017375744_n.jpg";

import pdfMain from "../Final Project UTS.pdf";

const highlights = [
  "Identity and self-management insights",
  "Evidence-based reflection from course modules",
  "Visual artifacts documented across milestones",
  "Final synthesis for UTS assessment"
];

const gallery = [
  { src: img1, alt: "Project visual artifact 1" },
  { src: img2, alt: "Project visual artifact 2" },
  { src: img3, alt: "Project visual artifact 3" },
  { src: img4, alt: "Project visual artifact 4" },
  { src: img5, alt: "Project visual artifact 5" }
];

const reflection = [
  "In navigating my personal and academic growth, one of the most profound realizations I have had is that self-care is not an optional luxury, but a foundational necessity. As the course highlights, you cannot pour from an empty cup, and I have learned that truly caring for myself means actively communicating with my soul to ask what it needs in the moment.",
  "Alongside this, discovering Albert Bandura's concept of self-efficacy, the belief in my own capability to learn and perform at designated levels, has shifted how I approach my goals. I now understand that as a student, my belief in my own abilities is an even stronger predictor of my academic achievement than my baseline skills.",
  "When life gets overwhelming, I now know how to differentiate between harmful distress and motivating eustress, and I realize the importance of stepping back to prevent burnout. For emotional and mental self-care, I pick up my guitar or listen to artists like Laufey, Adie, Maki, and other love song artists. These hobbies give me a peaceful space to relax, process my emotions, and attune to my inner being.",
  "Social self-care is equally important to me, so I intentionally carve out time to talk with my friends and stay connected with family. These routines do more than recharge my energy. They also build my self-efficacy through healthier stress management and social encouragement, giving me confidence to handle academic responsibilities.",
  "Ultimately, integrating self-care and self-efficacy has taught me to treat myself with the same compassion and kindness I would offer a friend. Whether I am strumming a love song on my guitar to unwind or pushing toward an academic milestone, I know my true competition is my own procrastination, ego, and negative habits. By honoring my imperfections and consistently nurturing my well-being, I am learning to focus not just on success, but on a life of significance."
];

export default function App() {
  return (
    <div className="page">
      <div className="grain" aria-hidden="true" />

      <header className="hero brutal-card reveal">
        <p className="tag">UNIVERSITY SHOWCASE</p>
        <h1>This Is My Life: Self-Care, Friends, Family, and Hobbies</h1>
        <p className="subtitle">
          My personal reflection on how self-care and self-efficacy shape my academic growth,
          emotional balance, and day-to-day life.
        </p>
        <div className="hero-actions">
          <a className="btn btn-yellow" href={pdfMain} target="_blank" rel="noreferrer">
            Open Final PDF in New Tab
          </a>
        </div>
      </header>

      <section className="section-grid">
        <article className="brutal-card reveal">
          <h2>Core Themes</h2>
          <ul className="list">
            {highlights.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </article>

        <article className="brutal-card accent reveal">
          <h2>My Practice of Self-Care</h2>
          <p>
            Emotional and mental care: guitar practice, music, and intentional pauses when stress
            rises.
          </p>
          <p>
            Social care: conversations with my friends and family to stay grounded and supported.
          </p>
        </article>
      </section>

      <section className="story-wrap brutal-card reveal">
        <h2>Reflection Narrative</h2>
        <div className="story-grid">
          {reflection.map((paragraph) => (
            <p className="story-block" key={paragraph.slice(0, 40)}>
              {paragraph}
            </p>
          ))}
        </div>
      </section>

      <section className="pdf-wrap brutal-card reveal">
        <div className="gallery-head">
          <h2>Document Viewer</h2>
          <p>The final PDF is shown directly here for easy in-page review.</p>
        </div>
        <div className="pdf-grid">
          <article className="pdf-card">
            <h3>Final Project PDF</h3>
            <iframe src={pdfMain} title="Final Project PDF" loading="lazy" />
          </article>
        </div>
      </section>

      <section className="gallery-wrap brutal-card reveal">
        <div className="gallery-head">
          <h2>Visual Evidence</h2>
          <p>Artifacts captured during the project process.</p>
        </div>

        <div className="gallery-grid">
          {gallery.map((photo, index) => (
            <figure className="gallery-item" key={photo.src} style={{ animationDelay: `${index * 90}ms` }}>
              <img src={photo.src} alt={photo.alt} loading="lazy" />
            </figure>
          ))}
        </div>
      </section>

      <footer className="footer reveal">
        <p>Built in React + Vite with a neobrutalist style to present my life reflection clearly.</p>
      </footer>
    </div>
  );
}