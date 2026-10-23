
const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const caption = document.getElementById("caption");
const loading = document.getElementById("loading");

imageInput.addEventListener("change", function () {
    const file = this.files[0]; 

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
        caption.textContent = "Ready to generate.";
    }
});

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        caption.textContent = "Please select an image.";
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    loading.textContent = "Generating caption...";
    caption.textContent = "";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        caption.textContent = data.caption;
    } catch (error) {
        caption.textContent = "Error: " + error.message;
    } finally {
        loading.textContent = "";
    }
});
