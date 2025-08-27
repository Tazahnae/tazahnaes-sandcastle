import { JSDOM } from 'jsdom';
const html = `<!doctype html><html><body>
<h1 id="title">Hello, STEAM!</h1>
<button id="btn">Change Text</button>
<script></script></body></html>`;
function runScript(window){
  window.document.getElementById('btn').addEventListener('click', () => {
    window.document.getElementById('title').textContent = 'You did it! 🎉';
  });
}
test('button click changes title', () => {
  const dom = new JSDOM(html, { runScripts: 'outside-only' });
  const { window } = dom;
  runScript(window);
  window.document.getElementById('btn').click();
  expect(window.document.getElementById('title').textContent).toBe('You did it! 🎉');
});
