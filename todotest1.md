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