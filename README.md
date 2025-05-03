# 🧾 HTML CV Generator from CSV Files

This project allows you to automatically generate a structured, stylish HTML resume by simply filling out a series of CSV files. It's built with Python and generates a print-ready CV using pre-defined templates and styling.

---

## 🚀 Features

- ✅ Structured resume building via modular CSV input
- ✅ Clean, A4-formatted HTML output with modern styling
- ✅ Auto logging to track errors and processing
- ✅ Easy to extend with additional sections (projects, publications, etc.)
- ✅ Uses Font Awesome icons and CSS styling
- ✅ Template.html included for previewing the CV layout
- ✅ PDF Export: Save your CV as a PDF by printing it directly from your browser

---

## 🗂️ Project Structure

```
.
├── cv_builder.py          # Main script for generating the resume
├── style.css              # CSS file used for HTML formatting
├── data/                  # Folder containing all CSV files
│   ├── personal_info.csv
│   ├── skills.csv
│   ├── education.csv
│   ├── experience.csv
│   ├── projects.csv
│   ├── achievements.csv
│   ├── publications.csv
│   └── languages.csv
├── CV_Result.html         # Output file (generated after running the script)
├── Template.html          # Preview template for the CV layout
├── cv_builder.log         # Log file for debugging
└── README.md              # This file
```

---

## 📥 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Resume-Generator-HTML-CSV.git
cd Resume-Generator-HTML-CSV
```

### 2. Install dependencies

```bash
pip install pandas
```

### 3. Prepare your CSV files

Fill out the CSV files in the `data/` folder. Each CSV file has a specific structure:

#### Example: `personal_info.csv`

| name     | profession      | phone      | location | email           | github                  | linkedin                |
|----------|------------------|------------|----------|------------------|--------------------------|--------------------------|
| John Doe | Software Engineer| 1234567890 | NY, USA  | john@example.com| https://github.com/johndoe | https://linkedin.com/in/johndoe |

#### Example: `skills.csv`

| skill    | type                   |
|----------|------------------------|
| Python   | Programming Languages  |
| Docker   | Technical Knowledge    |

> The `type` column should be either `Programming Languages` or `Technical Knowledge`.

---

## 🏗️ CSV Format Summary

| File                | Description                         |
|---------------------|-------------------------------------|
| `personal_info.csv` | Basic personal and contact info     |
| `skills.csv`        | Technical and programming skills    |
| `education.csv`     | Education history                   |
| `experience.csv`    | Work experience                     |
| `projects.csv`      | Key personal/professional projects  |
| `achievements.csv`  | Awards or honors                    |
| `publications.csv`  | Published work                      |
| `languages.csv`     | Spoken language proficiency         |

---

## ▶️ Run the Generator

```bash
python cv_builder.py
```

The output file will be created as `CV_Result.html`.

---

## 🛠️ Customization

- Modify `style.css` to change layout, fonts, or colors.
- Extend `CVBuilder` class in `cv_builder.py` to add new CV sections.
- You can integrate themes or templates by customizing the HTML output structure.

---

## 🧪 Sample Output

The script will generate a file like this:

```
CV_Result.html
```

You can open this in any browser or print it as a PDF.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it for personal or professional purposes.

---
