# 📚 Book Store Microservices Project

This repository contains the **Book Store Distributed System**, a microservices-based project developed for the *Distributed Software Systems* course (2025/2026).  
Students will work collaboratively to implement different services, including **Users**, **Books**, and **Orders**, using **Flask**, **PostgreSQL**, **Docker Compose**, and **Nginx**.

---

## 🚀 Project Overview

### 🧩 Microservices

- **Users Service** — Registration, authentication, user management  
- **Books Service** — CRUD operations for books  
- **Orders Service** — Creating and listing book orders  

### 🧱 Infrastructure

- **PostgreSQL** — Central database  
- **Nginx** — Load balancer and reverse proxy  

---

## 🗂️ Working with the Repository

### 🔀 Branch Structure

- **`main`** — The stable branch (do not push directly here).  
- **Feature branches** — Create a new branch for every task or story.  
  - Naming convention:  
    ```
    feature/<short-description>
    ```
    Example:
    ```
    feature/implement-books-endpoints
    bugfix/fix-delete-book-endpoint
    ```

---

## 🧑‍💻 Workflow

### 1️⃣  Clone the Repository

```bash
git clone https://github.com/<org>/bookstore-project.git
cd bookstore-project
```

### 2️⃣  Use the predifined branches for the feature or create a new one

```bash
git checkout feature/implement-books-endpoints # Switch to existing branch
OR 
git checkout -b bugfix/fix-delete-book-endpoint # Create a new branch with the given name
```

### 3️⃣  Work on Your feature

Implement your assigned issue (check the GitHub Project Board for tasks).

### 4️⃣  Commit Your Changes

Use clear and meaningful commit messages following this convention:

```bash
<type>: <short description>

Example:
feat: add user registration endpoint
fix: correct DB connection URL in users service
docs: update README with setup instructions
refactor: clean up Flask app structure
```

### :five: Opening Pull Requests (PRs)

Push your branch to GitHub:

```bash
git push origin feature/<your-name>/<task-name>
```

Open a Pull Request from your branch → master
Use the provided PR template
Assign yourself and add reviewers
Wait for code review and approval before merging

### 🧹 Clean Code Guidelines

* ✅ Use consistent indentation and naming conventions
* 🧠 Keep functions short and single-purpose
* 📄 Add docstrings and comments for clarity
* 🧪 Test your code locally before committing
* 🚫 Avoid hard-coded values — use configuration variables
* 🧼 Remove unused imports, debug prints, and commented code


### 🧠 Tips for Collaboration

* Use Issues to track bugs or feature requests
* Reference issues in commits and PRs: Closes #5
* Communicate regularly with your team and raise GitHub issues if needed
