# XSS and Purification Test Cases for HeyFred Chat

## 🔒 Security Test Cases

### 1. Basic Script Injection Tests
Test these messages in your chat to ensure scripts are blocked:

```markdown
<script>alert('XSS')</script>
```

```markdown
<img src="x" onerror="alert('XSS')">
```

```markdown
<svg onload="alert('XSS')">
```

```markdown
javascript:alert('XSS')
```

**Expected Result:** No alerts should appear, content should be safely rendered or escaped.

### 2. Event Handler Tests
```markdown
<div onclick="alert('XSS')">Click me</div>
```

```markdown
<p onmouseover="alert('XSS')">Hover over me</p>
```

```markdown
<input onfocus="alert('XSS')" autofocus>
```

**Expected Result:** Event handlers should be stripped, only safe HTML should remain.

### 3. Style and CSS Injection Tests
```markdown
<style>body { background: red; }</style>
```

```markdown
<div style="background: url(javascript:alert('XSS'))">Test</div>
```

```markdown
<link rel="stylesheet" href="javascript:alert('XSS')">
```

**Expected Result:** Style tags and dangerous CSS should be removed.

### 4. iFrame and Embed Tests
```markdown
<iframe src="javascript:alert('XSS')"></iframe>
```

```markdown
<object data="javascript:alert('XSS')"></object>
```

```markdown
<embed src="javascript:alert('XSS')">
```

**Expected Result:** These tags should be completely removed.

### 5. Link and URL Tests
```markdown
[Click me](javascript:alert('XSS'))
```

```markdown
[Normal link](https://example.com)
```

```markdown
<a href="javascript:alert('XSS')">Dangerous link</a>
```

**Expected Result:** Dangerous URLs should be blocked, normal links should work.

### 6. Data URL Tests
```markdown
<img src="data:text/html,<script>alert('XSS')</script>">
```

```markdown
[Data URL](data:text/html,<script>alert('XSS')</script>)
```

**Expected Result:** Malicious data URLs should be blocked.

## ✅ Legitimate Markdown Tests

### 1. Basic Markdown Features
Test these to ensure normal markdown still works:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough~~

- List item 1
- List item 2
- List item 3

1. Numbered item 1
2. Numbered item 2
3. Numbered item 3
```

### 2. Code Blocks and Syntax Highlighting
```markdown
Here's some inline `code`.

```python
def hello_world():
    print("Hello, World!")
    return True
```

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```

```html
<div class="container">
    <h1>Title</h1>
    <p>Paragraph</p>
</div>
```
```

### 3. Tables
```markdown
| Name | Age | City |
|------|-----|------|
| Alice | 30 | New York |
| Bob | 25 | London |
| Charlie | 35 | Tokyo |
```

### 4. Links and Images
```markdown
[Google](https://www.google.com)
[GitHub](https://github.com)

Normal text with automatic link detection: https://www.example.com
```

### 5. Blockquotes and Horizontal Rules
```markdown
> This is a blockquote
> It can span multiple lines
> And contain other formatting like **bold**

---

This is after a horizontal rule.
```

## 🧪 Edge Case Tests

### 1. Mixed Content Tests
```markdown
# Heading with <script>alert('XSS')</script>

Here's a paragraph with **bold** and <img src="x" onerror="alert('XSS')"> text.

```python
# This is safe code
print("<script>alert('safe')</script>")
```
```

### 2. Nested Attacks
```markdown
<div><script>alert('XSS')</script></div>
```

```markdown
<p onclick="alert('XSS')">Paragraph with <strong>bold</strong> text</p>
```

### 3. URL Encoding Tests
```markdown
<img src="x" onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;">
```

### 4. Unicode and Special Characters Tests
```markdown
<script>alert('XSS')</script>
<scr\x00ipt>alert('XSS')</scr\x00ipt>
```

## 📋 Manual Testing Checklist

### Pre-Test Setup
- [ ] Open browser developer tools (F12)
- [ ] Go to Console tab to watch for any executed scripts
- [ ] Clear console before each test

### For Each Test Case
- [ ] Copy the test case into the chat input
- [ ] Send the message
- [ ] Check that no alert boxes appear
- [ ] Check that no JavaScript errors occur in console
- [ ] Verify the content renders safely (malicious parts removed)
- [ ] Check that legitimate markdown features still work correctly

### Browser Testing
Test in multiple browsers:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### Performance Testing
- [ ] Send multiple large markdown messages quickly
- [ ] Verify no memory leaks with long conversations
- [ ] Test with very long code blocks
- [ ] Test with deeply nested markdown structures

## 🚨 What to Look For

### Signs of Successful XSS Prevention:
- No alert boxes appear when testing malicious scripts
- Dangerous HTML tags are completely removed
- Event handlers (onclick, onload, etc.) are stripped
- Malicious URLs are blocked or sanitized
- Console shows no JavaScript execution errors

### Signs of Proper Markdown Rendering:
- Headings render with proper hierarchy
- Code blocks have syntax highlighting
- Lists and tables display correctly
- Links work for legitimate URLs
- Formatting (bold, italic) works properly

### Red Flags (Contact Developer Immediately):
- Any alert boxes appear during testing
- Malicious scripts execute in any form
- Console shows XSS-related errors
- Legitimate content is broken or not rendering
- Performance significantly degrades

## 🔄 Continuous Testing

### Regular Checks:
1. Test new markdown features when added
2. Verify after any library updates
3. Test with real-world content examples
4. Check after any changes to the markdown processing code

### Automated Testing Considerations:
While manual testing is crucial, consider adding:
- Unit tests for the renderMarkdown function
- Integration tests for the full message flow
- Automated XSS scanning tools
- Regular security audits