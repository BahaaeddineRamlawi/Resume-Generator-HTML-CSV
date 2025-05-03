import pandas as pd
import logging

logging.basicConfig(
    filename="cv_builder.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class CVBuilder:
    def __init__(self, base_path=""):
        self.base_path = base_path
        self.html = ""
        try:
            self.load_data()
            self.extract_personal_info()
        except Exception as e:
            logging.exception("Initialization failed.")
            raise

    def read_csv(self, filename):
        try:
            df = pd.read_csv(f"{self.base_path}{filename}")
            logging.info(f"Loaded '{filename}' successfully.")
            return df
        except FileNotFoundError:
            logging.warning(f"File not found: {filename}")
            return pd.DataFrame()
        except Exception:
            logging.exception(f"Error reading file: {filename}")
            return pd.DataFrame()

    def load_data(self):
        try:
            self.personal_info_df = self.read_csv("data/personal_info.csv")
            if self.personal_info_df.empty:
                logging.error("personal_info.csv is required but not found or empty.")
                raise ValueError("personal_info.csv is required.")

            self.skills_df = self.read_csv("data/skills.csv")
            self.education_df = self.read_csv("data/education.csv")
            self.experience_df = self.read_csv("data/experience.csv")
            self.projects_df = self.read_csv("data/projects.csv")
            self.achievements_df = self.read_csv("data/achievements.csv")
            self.publications_df = self.read_csv("data/publications.csv")
            self.languages_df = self.read_csv("data/languages.csv")
        except Exception:
            logging.exception("Failed to load data.")
            raise

    def extract_personal_info(self):
        try:
            info = self.personal_info_df.iloc[0]
            self.name = info["name"]
            self.profession = info["profession"]
            self.phone = info["phone"]
            self.location = info["location"]
            self.email = info["email"]
            self.github = info["github"]
            self.linkedin = info["linkedin"]
            logging.info("Extracted personal info.")
        except Exception:
            logging.exception("Failed to extract personal info.")
            raise

    def build_header(self):
        try:
            self.html += f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{self.name} CV</title>
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
<div class="cv">
  <div class="first-section">
    <div class="name-profession">
      <h1>{self.name}</h1>
      <h3>{self.profession}</h3>
    </div>
    <div class="contact-info">
      <div class="column">
        <p><i class="fas fa-phone"></i> {self.phone}</p>
        <p><i class="fas fa-map-marker-alt"></i> {self.location}</p>
      </div>
      <div class="column">
        <p><i class="fas fa-envelope"></i> <a href="mailto:{self.email}">{self.email}</a></p>
        <p><i class="fab fa-github"></i> <a href="{self.github}" target="_blank">{self.github.replace("https://", "")}</a></p>
        <p><i class="fab fa-linkedin"></i> <a href="{self.linkedin}" target="_blank">{self.name}</a></p>
      </div>
    </div>
  </div>
"""
            logging.info("Header section built.")
        except Exception:
            logging.exception("Failed to build header.")

    def build_skills(self):
        try:
            if self.skills_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ SKILLS</h2>\n'

            prog_df = self.skills_df[self.skills_df["type"] == "Programming Languages"]
            if not prog_df.empty:
                self.html += '<p><strong>Programming Languages:</strong></p>\n<div class="skills">\n'
                for _, row in prog_df.iterrows():
                    self.html += f'<span>{row["skill"]}</span>\n'
                self.html += '</div>\n'

            tech_df = self.skills_df[self.skills_df["type"] == "Technical Knowledge"]
            if not tech_df.empty:
                skills = ', '.join(tech_df["skill"].tolist())
                self.html += f'<p><strong>Technical Knowledge:</strong></p>\n<p id="description">{skills}.</p>\n'

            self.html += '</div>\n'
            logging.info("Skills section built.")
        except Exception:
            logging.exception("Failed to build skills section.")

    def build_education(self):
        try:
            if self.education_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ EDUCATION</h2>\n'
            for _, row in self.education_df.iterrows():
                self.html += f"""
        <p class="info-line">
          <span class="bold-title"><a href="{row['url']}">{row['institution']}</a></span>
          <span class="date">{row['date']}</span>
        </p>
        <p id="description">{row['description']}</p>
        """
            self.html += '</div>\n'
            logging.info("Education section built.")
        except Exception:
            logging.exception("Failed to build education section.")

    def build_experience(self):
        try:
            if self.experience_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ EXPERIENCE</h2>\n'
            for _, row in self.experience_df.iterrows():
                self.html += f"""
        <p class="info-line">
          <span class="bold-title">{row['title']}</span>
          <span class="date">{row['date']}</span>
        </p>
        <p id="description">{row['description']}</p>
        """
            self.html += '</div>\n'
            logging.info("Experience section built.")
        except Exception:
            logging.exception("Failed to build experience section.")

    def build_achievements(self):
        try:
            if self.achievements_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ SPECIAL ACHIEVEMENT</h2>\n'
            for _, row in self.achievements_df.iterrows():
                self.html += f"""
        <p class="info-line">
          <span class="bold-title"><a href="{row['url']}">{row['title']}</a></span>
          <span class="date">{row['date']}</span>
        </p>
        <p id="description">{row['description']}</p>
        """
            self.html += '</div>\n'
            logging.info("Achievements section built.")
        except Exception:
            logging.exception("Failed to build achievements section.")

    def build_projects(self):
        try:
            if self.projects_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ PROJECTS</h2>\n'
            for _, row in self.projects_df.iterrows():
                title = row["title"]
                subtitle = row["subtitle"] if pd.notna(row["subtitle"]) and row["subtitle"].strip() else None
                date = row["date"]
                description = row["description"]

                self.html += '<p class="info-line">\n'
                if subtitle:
                    self.html += f'''
            <span class="bold-title">
              <span class="underline-text">{title}</span>: {subtitle}
            </span>
            <span class="date">{date}</span>
            </p>\n'''
                else:
                    self.html += f'''
            <span class="bold-title">{title}</span>
            <span class="date">{date}</span>
            </p>\n'''

                self.html += f'<p id="description">{description}</p>\n'
            self.html += '</div>\n'
            logging.info("Projects section built.")
        except Exception:
            logging.exception("Failed to build projects section.")

    def build_publications(self):
        try:
            if self.publications_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ PUBLICATIONS</h2>\n'
            for _, row in self.publications_df.iterrows():
                self.html += f"""
        <p class="info-line">
          <span class="bold-title">Authors: {row['authors']}</span>
        </p>
        <p id="description"><a href="{row['url']}">{row['title']}</a><br>{row['description']}</p>
        """
            self.html += '</div>\n'
            logging.info("Publications section built.")
        except Exception:
            logging.exception("Failed to build publications section.")

    def build_languages(self):
        try:
            if self.languages_df.empty:
                return
            self.html += '<div class="section">\n<h2>◈ LANGUAGES</h2>\n<div class="languages">\n'
            for _, row in self.languages_df.iterrows():
                self.html += f"""
        <div class="language-item">
          <span class="language-name">{row['language']}</span>
          <span class="language-level">{row['level']}</span>
        </div>
        """
            self.html += '</div>\n</div>\n'
            logging.info("Languages section built.")
        except Exception:
            logging.exception("Failed to build languages section.")

    def generate_html(self, filename="CV_Result.html"):
        try:
            self.build_header()
            self.build_skills()
            self.build_education()
            self.build_experience()
            self.build_achievements()
            self.build_projects()
            self.build_publications()
            self.build_languages()
            self.html += "</div>\n</body>\n</html>"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.html)
            logging.info(f"CV generated successfully in '{filename}'.")
            print(f"CV generated successfully in '{filename}'")
        except Exception:
            logging.exception("Failed to generate HTML CV.")
            print("An error occurred. Check logs for details.")

if __name__ == "__main__":
    try:
        builder = CVBuilder()
        builder.generate_html()
    except Exception:
        logging.critical("Fatal error in main execution.", exc_info=True)
        print("Fatal error. Check cv_builder.log for details.")
