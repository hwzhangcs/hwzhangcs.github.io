# Portrait

The site uses `images/portrait.jpg` (480 × 600, about 44 KB): a 4:5 head-and-shoulders crop
for the homepage hero, the author avatar setting and the social link preview (`og_image`).

## Source

1. Original photo: `images/profile-sunset.jpg` (4032 × 3024).
2. Lighting edit: `images/profile-sunset-light.png` (1448 × 1086), a subtle local exposure lift on the face
   made with the built-in image_gen tool. Identity, expression, sky and framing were preserved; no beautification.
3. Crop: 480 × 600 px source region at (200, 200) of the lit image, exported as JPEG quality 84.

Both source files were removed from the working tree on September 26, 2026 because the site no longer loads them.
They remain in git history (last present in commit 46d4bb1): `git show 46d4bb1:images/profile-sunset-light.png > lit.png`.
