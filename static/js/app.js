(function () {
  const root = document.documentElement;
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const themeIcon = document.querySelector("[data-theme-icon]");

  function setTheme(theme) {
    root.dataset.theme = theme;
    localStorage.setItem("theme", theme);
    if (themeIcon) {
      themeIcon.textContent = theme === "dark" ? "Light" : "Dark";
    }
  }

  setTheme(localStorage.getItem("theme") || "light");

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      setTheme(root.dataset.theme === "dark" ? "light" : "dark");
    });
  }

  const sourceText = document.querySelector("[data-source-text]");
  const resultText = document.querySelector("[data-result-text]");
  const sourceLanguage = document.querySelector("#source_language");
  const targetLanguage = document.querySelector("#target_language");
  const wordCount = document.querySelector("[data-word-count]");
  const charCount = document.querySelector("[data-char-count]");
  const copyStatus = document.querySelector("[data-copy-status]");

  function updateCounts() {
    if (!sourceText) {
      return;
    }
    const text = sourceText.value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    if (wordCount) {
      wordCount.textContent = `${words} ${words === 1 ? "word" : "words"}`;
    }
    if (charCount) {
      charCount.textContent = `${sourceText.value.length} characters`;
    }
  }

  if (sourceText) {
    sourceText.addEventListener("input", updateCounts);
    updateCounts();
  }

  const clearSource = document.querySelector("[data-clear-source]");
  if (clearSource && sourceText) {
    clearSource.addEventListener("click", function () {
      sourceText.value = "";
      if (resultText) {
        resultText.value = "";
      }
      updateCounts();
      sourceText.focus();
    });
  }

  const swapButton = document.querySelector("[data-swap-languages]");
  if (swapButton && sourceLanguage && targetLanguage && sourceText && resultText) {
    swapButton.addEventListener("click", function () {
      if (sourceLanguage.value !== "auto") {
        const sourceValue = sourceLanguage.value;
        sourceLanguage.value = targetLanguage.value;
        targetLanguage.value = sourceValue;
      }
      const sourceValue = sourceText.value;
      sourceText.value = resultText.value;
      resultText.value = sourceValue;
      updateCounts();
    });
  }

  const copyButton = document.querySelector("[data-copy-result]");
  if (copyButton && resultText) {
    copyButton.addEventListener("click", async function () {
      const value = resultText.value.trim();
      if (!value) {
        return;
      }
      await navigator.clipboard.writeText(value);
      if (copyStatus) {
        copyStatus.textContent = "Copied";
        window.setTimeout(function () {
          copyStatus.textContent = "";
        }, 1400);
      }
    });
  }

  const downloadButton = document.querySelector("[data-download-text]");
  if (downloadButton && resultText && sourceText) {
    downloadButton.addEventListener("click", function () {
      const content = `Source:\n${sourceText.value}\n\nTranslation:\n${resultText.value}\n`;
      const blob = new Blob([content], { type: "text/plain" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "translation.txt";
      link.click();
      URL.revokeObjectURL(link.href);
    });
  }

  document.querySelectorAll("[data-history-source]").forEach(function (item) {
    item.addEventListener("click", function () {
      if (sourceText) {
        sourceText.value = item.dataset.historySource || "";
      }
      if (resultText) {
        resultText.value = item.dataset.historyResult || "";
      }
      updateCounts();
    });
  });

  const historySearch = document.querySelector("[data-history-search]");
  const historyFilter = document.querySelector("[data-history-filter]");
  const historyRows = Array.from(document.querySelectorAll("[data-search-text]"));

  function filterHistory() {
    const query = historySearch ? historySearch.value.trim().toLowerCase() : "";
    const target = historyFilter ? historyFilter.value : "";
    historyRows.forEach(function (row) {
      const matchesQuery = row.dataset.searchText.toLowerCase().includes(query);
      const matchesTarget = !target || row.dataset.targetLanguage === target;
      row.hidden = !(matchesQuery && matchesTarget);
    });
  }

  if (historySearch) {
    historySearch.addEventListener("input", filterHistory);
  }
  if (historyFilter) {
    historyFilter.addEventListener("change", filterHistory);
  }
})();
