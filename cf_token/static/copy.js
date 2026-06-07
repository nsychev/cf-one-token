const btn = document.getElementById("copy");

if (btn) {
    btn.addEventListener("click", async () => {
        const token = document.getElementById("token").textContent;
        try {
            await navigator.clipboard.writeText(token);
        } catch (e) {
            const range = document.createRange();
            range.selectNodeContents(document.getElementById("token"));
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
            document.execCommand("copy");
        }
        const original = btn.textContent;
        btn.textContent = "Copied!";
        btn.disabled = true;
        setTimeout(() => {
            btn.textContent = original;
            btn.disabled = false;
        }, 1500);
    });
}
