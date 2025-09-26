# DevOps Example Project (Python + Eclipse + GitHub)

This project demonstrates a **version-controlled DevOps workflow** using **Python**, **Eclipse (EGit)**, and **GitHub**, with proper branching, commits, pull requests, merging, tags, and `.gitignore` management.

---

## 🚀 Workflow Overview
- **main** → Production-ready branch  
- **dev** → Integration/testing branch  
- **feature/** → Individual development feature branch

---

## 🔹 Steps Completed

1. **Project Setup in Eclipse**  
   - Created a Python project in Eclipse.  
   - Added a local Git repository.

2. **Main Branch**  
   - Added initial Python file in `main` branch.  
   - Committed initial code.

3. **Branch Creation**  
   - Created `dev` branch with `main` as source.  
   - Created `feature/login-page` branch with `dev` as source.  

4. **Feature Development**  
   - Modified the Python file in the `feature/login-page` branch.  
   - Committed the changes.

5. **Pushing Branches to GitHub**  
   - Pushed `feature/login-page` branch to GitHub.  
   - Pushed `dev` and `main` branches to GitHub.

6. **Pull Requests and Merging**  
   - Opened a PR on GitHub: `feature/login-page → dev`.  
   - Merged feature branch into `dev`.  
   - Opened a PR: `dev → main`.  
   - Merged `dev` into `main`.  
   ✅ All branches successfully merged.

7. **Tags and .gitignore**  
   - Added tags for release versions.  
   - Added `.gitignore` to exclude unnecessary files.

---

## 🔧 .gitignore Example
```gitignore
__pycache__/
*.pyc
*.pyo
.env
.vscode/


