# Raspberry Pi Camera & Remote Access Setup

This repository documents the setup, configuration, and troubleshooting steps used to prepare a Raspberry Pi for a camera‑based computer vision project.  
It includes SSH setup, password recovery, system updates, camera testing, and environment preparation.

---

## 🚀 Project Overview

This project uses a Raspberry Pi as a remote camera platform for future computer‑vision work (e.g., wildlife or predator detection).  
The Pi is accessed remotely over SSH, allowing it to operate without a monitor, keyboard, or mouse.

---

## 📦 Requirements

- Raspberry Pi (any model with camera support)
- Raspberry Pi OS (Bookworm or later recommended)
- Camera Module (official or compatible)
- SSH enabled
- Laptop/desktop for remote access (Linux, macOS, or Windows)

---

## 🔐 SSH Access

### Connect to the Raspberry Pi
```bash
ssh hans@192.168.1.22# predator-detection