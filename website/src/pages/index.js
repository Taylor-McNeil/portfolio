import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout
      title="Technical Writing & Portfolio"
      description="Showcasing skills in API documentation, automation, and SDK development"
    >
      <main>
        <section style={{ padding: '2rem 0', textAlign: 'center' }}>
          <h1>Welcome to My Technical Writing & Developer Advocacy Portfolio</h1>
          <p>
            I specialize in creating clear, developer-friendly documentation, 
            automating Docs-as-Code workflows, and integrating SDKs for robust 
            APIs. Explore my work to see how I make complex concepts accessible.
          </p>
        </section>

        <section style={{ padding: '2rem', backgroundColor: '#f9f9f9' }}>
  <h2>Explore My Skills</h2>
  <div style={{
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '1.5rem',
  }}>
    <div style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '1rem',
      backgroundColor: '#fff',
    }}>
      <h3>API Development</h3>
      <p>See how I build, deploy, and document APIs.</p>
      <Link to="/skills/api-development" style={{
        textDecoration: 'none',
        color: '#0078D7',
      }}>Explore</Link>
    </div>
    <div style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '1rem',
      backgroundColor: '#fff',
    }}>
      <h3>Docs-as-Code</h3>
      <p>Discover my automated workflows and CI/CD practices.</p>
      <Link to="/skills/docs-as-code" style={{
        textDecoration: 'none',
        color: '#0078D7',
      }}>Explore</Link>
    </div>
    <div style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '1rem',
      backgroundColor: '#fff',
    }}>
      <h3>SDK Development</h3>
      <p>Check out my SDKs and interactive tutorials.</p>
      <Link to="/skills/sdk-development" style={{
        textDecoration: 'none',
        color: '#0078D7',
      }}>Explore</Link>
    </div>
  </div>
</section>

        <section style={{ padding: '2rem' }}>
          <h2>Tools & Technologies</h2>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            <li>🖥️ Docusaurus</li>
            <li>🔧 GitHub Actions</li>
            <li>🛡️ Postman</li>
            <li>🧑‍💻 FastAPI, MongoDB</li>
          </ul>
        </section>

          <section style={{ padding: '2rem', backgroundColor: '#f1f1f1' }}>
          <h2 style={{textAlign: 'center' }}>Explore My Projects</h2>
              <p>
            Click below to dive into my projects and see the interactive demos, 
            detailed documentation, and live integrations.
          </p>
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                gap: '1.5rem',
              }}>
                <div style={{
                  border: '1px solid #ddd',
                  borderRadius: '8px',
                  padding: '1rem',
                  backgroundColor: '#fff',
                }}>
                  <h3>Project 1: REST API</h3>
                  <p>Build and document a REST API with MongoDB integration.</p>
                  <Link to="/projects/rest-api" style={{
                    textDecoration: 'none',
                    color: '#0078D7',
                  }}>Learn More</Link>
                </div>
                <div style={{
                  border: '1px solid #ddd',
                  borderRadius: '8px',
                  padding: '1rem',
                  backgroundColor: '#fff',
                }}>
                  <h3>Project 2: GraphQL Integration</h3>
                  <p>Develop and document a GraphQL API alongside REST endpoints.</p>
                  <Link to="/projects/graphql-api" style={{
                    textDecoration: 'none',
                    color: '#0078D7',
                  }}>Learn More</Link>
                </div>
                <div style={{
                  border: '1px solid #ddd',
                  borderRadius: '8px',
                  padding: '1rem',
                  backgroundColor: '#fff',
                }}>
                  <h3>Project 3: SDK Development</h3>
                  <p>Create and document an SDK with interactive tutorials.</p>
                  <Link to="/projects/sdk-development" style={{
                    textDecoration: 'none',
                    color: '#0078D7',
                  }}>Learn More</Link>
                </div>
                {/* Add additional cards for Projects 4-6 */}
              </div>
            </section>
      </main>
    </Layout>
  );
}
