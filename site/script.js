document.querySelectorAll("[data-copy]").forEach((button) => {
  if (!navigator.clipboard || !window.isSecureContext) return;
  button.hidden = false;
  button.addEventListener("click", async () => {
    const status = document.getElementById("copy-status");
    try {
      await navigator.clipboard.writeText(
        document.getElementById(button.dataset.copy).textContent,
      );
      status.textContent = "Commands copied to clipboard.";
      const label = button.textContent;
      button.textContent = "Copied";
      button.disabled = true;
      setTimeout(() => {
        button.textContent = label;
        button.disabled = false;
      }, 1800);
    } catch {
      status.textContent =
        "Copy unavailable. Select and copy the commands above.";
    }
  });
});
