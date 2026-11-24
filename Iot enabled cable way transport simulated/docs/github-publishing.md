# Publishing to GitHub

```bash
cd iot-cableway-fusion360
git init
git lfs install                 # for .stl/.f3d/.step (see .gitattributes)
git add .
git commit -m "Initial commit: concept models, guides, hand-check tool"
git branch -M main
git remote add origin https://github.com/<your-username>/iot-cableway-fusion360.git
git push -u origin main
```

Tips
- Commit after each completed model or simulation so the history shows real progress.
- Keep the patent description to "filed, awaiting examination". Confirm with co-inventors before publishing design detail.
- Replace `<your-username>` in the resume link with your real GitHub username.
- If the repo gets heavy, keep screenshots, tables and STEP files, and skip raw `.f3d`.
