#  Ubuntu Image Fetcher

**“I am because we are.”**  
A mindful tool for collecting and organizing shared images from the web, inspired by the Ubuntu philosophy of community, respect, and connection.

---

##  About

Ubuntu Image Fetcher is a Python script that gently connects to the global web community, fetches publicly shared images, and organizes them into a local folder for later appreciation. It’s designed with care, clarity, and the spirit of Ubuntu—emphasizing collaboration, respect for others’ work, and thoughtful digital stewardship.

---

## Features

-  Fetches images from one or multiple URLs
- Saves them in a `Fetched_Images` directory
- Prevents duplicate downloads
- Validates image content before saving
- Provides clear, respectful feedback in the terminal

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Flora72/week6_python
   cd week6_python
   ```

2. Run the script:
   ```bash
   python3 index.py
   ```

3. When prompted, enter one or more image URLs (comma-separated):
   ```
   https://img.icons8.com/hands/100/trust.png, https://upload.wikimedia.org/wikipedia/commons/5/5b/Ubuntu_logo.svg
   ```

4. Watch as the script gently fetches and organizes each image.

---

##  Ubuntu Principles in Action

| Principle     | Implementation                                                |
|---------------|---------------------------------------------------------------|
| **Community** | Connects to the global web to gather shared resources         |
| **Respect**   | Handles errors gracefully, never crashes                      |
| **Sharing**   | Organizes images for future use and appreciation              |
| **Practicality** | Offers a real-world tool for mindful digital collection   |

---

## Folder Structure

```
Week6/
├── index.py
├── README.md
└── Fetched_Images/
    └── [downloaded images]
```

---

## Requirements

- Python 3.x
- `requests` library  
  Install with:
  ```bash
  pip install requests
  ```

---

## Screenshot

To visualize the Ubuntu Image Fetcher tool in action, here are a few screenshots:
### Ubuntu Image Fetcher in action
![Ubuntu Image Fetcher in action](https://github.com/user-attachments/assets/b5ba4e23-33fb-4b55-a329-50a38cdecbe1)
### Fetched Images
![Fetched_images](https://github.com/user-attachments/assets/c06e8fe4-505e-45df-9a13-fd5cdc8e82b0)

