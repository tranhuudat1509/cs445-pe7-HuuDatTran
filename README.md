
# PE07 – SQL Injection Demonstration and Mitigation

**Huu Dat Tran**  
**CS445 – Software Process Management**  
**Instructor: Marcelo Guerra Hahn**  
**Date: 5/28/2025**

---

## Part 1 – Running the Application and Performing SQL Injection

### Question 1: What are the inputs and outputs?

**Inputs:**  
- Username: `Alice`  
- Password: `alice@1234`

**Outputs:**  
- Login successful!

---

## Part 2 – Running the SQL Injection

### Question 2: What inputs did you use to bypass authentication?

```plaintext
Username: ' OR 'a'='a
Password: 
```

---

### Question 3: Why do you think those inputs were successful in bypassing authentication?

The input bypassed authentication because the SQL query becomes:

```sql
SELECT * FROM users WHERE username = '' OR 'a'='a';
```

This condition is always true, allowing unauthorized login.

---

## Part 3 – Fixing the Application

### Question 4: What changes did you make to fix the code?

I replaced string interpolation in the SQL query with parameterized queries to prevent SQL injection. Here's the difference:

**Before (vulnerable):**
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
```

**After (secure):**
```python
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))
```

---

### Question 5: What are the new inputs and outputs?

**Inputs:**
```plaintext
Username: ' OR 'a'='a
Password: 
```

**Outputs:**
```plaintext
Invalid username or password.
```

---

## Notes

- This exercise reused the database schema from PE04.
- Docker and Docker Compose were used for deployment.
- Files used: `main_app.py`, `test_app.py`, `Dockerfile`, `docker-compose.yml`.
- Screenshots of testing, injection attempts, and fixed behavior were captured for validation.
