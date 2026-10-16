const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const SCAN_DIRS = ["research", "research/companies"];
const OUT = path.join(__dirname, "data.json");

function extractTitle(text) {
  const m = text.match(/^#\s+(.+)$/m);
  return m ? m[1].trim() : null;
}

function extractDate(text) {
  // 支援兩種格式："**標籤**：日期" 跟 "**標籤：**日期"
  const m = text.match(/\*\*(?:更新日期|報告日期)[：:]?\*\*[：:]?\s*(\d{4}-\d{2}-\d{2})/);
  return m ? m[1] : null;
}

function extractCode(filename) {
  const m = filename.match(/(\d{4,6})/);
  return m ? m[1] : null;
}

const reports = [];

for (const dir of SCAN_DIRS) {
  const full = path.join(ROOT, dir);
  if (!fs.existsSync(full)) continue;
  for (const f of fs.readdirSync(full)) {
    if (!f.endsWith(".md")) continue;
    const fullPath = path.join(full, f);
    if (fs.statSync(fullPath).isDirectory()) continue;
    const text = fs.readFileSync(fullPath, "utf8");
    const code = extractCode(f);
    if (!code) continue; // skip non-company notes (mind maps, prompts, etc.)
    const relPath = path.join(dir, f).replace(/\\/g, "/");
    reports.push({
      title: extractTitle(text) || f.replace(/\.md$/, ""),
      code,
      date: extractDate(text),
      path: "../" + relPath,
    });
  }
}

fs.writeFileSync(OUT, JSON.stringify(reports, null, 2) + "\n");
console.log(`Wrote ${reports.length} reports to ${OUT}`);
