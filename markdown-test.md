# Comprehensive Markdown Test

## Headers and Text Formatting

This is a **bold statement** and this is *italic text*. You can also combine them for ***bold and italic***.

### Subheading Level 3

Here's a paragraph with `inline code` and a [link to Google](https://www.google.com).

#### Subheading Level 4

Regular paragraph text with some ~~strikethrough~~ content.

---

## Lists and Structure

### Unordered List:
- First item with **bold text**
- Second item with *italic text*
- Third item with `inline code`
  - Nested item one
  - Nested item two

### Ordered List:
1. First numbered item
2. Second numbered item with a [link](https://example.com)
3. Third numbered item
   1. Nested numbered item
   2. Another nested item

## Code Blocks

### Python Example:
```python
def fibonacci(n):
    """Generate fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

# Test the function
result = fibonacci(10)
print(f"Fibonacci sequence: {result}")
```

### JavaScript Example:
```javascript
class Calculator {
    constructor() {
        this.result = 0;
    }
    
    add(value) {
        this.result += value;
        return this;
    }
    
    multiply(value) {
        this.result *= value;
        return this;
    }
    
    getResult() {
        return this.result;
    }
}

// Usage example
const calc = new Calculator();
const result = calc.add(5).multiply(3).getResult();
console.log(`Result: ${result}`); // Result: 15
```

### CSS Example:
```css
.message-content {
    line-height: 1.6;
    color: #333;
    font-family: 'Inter', sans-serif;
}

.code-block {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
}

@media (max-width: 768px) {
    .message-content {
        font-size: 14px;
    }
}
```

## Blockquotes

> This is a blockquote with some important information.
> It can span multiple lines and contain other formatting.
> 
> > This is a nested blockquote
> > with **bold text** and *italic text*.

> **Note:** Blockquotes are great for highlighting important information or quotes from other sources.

## Tables

| Feature | Status | Notes |
|---------|--------|-------|
| Headers | ✅ Working | All levels supported |
| Lists | ✅ Working | Both ordered and unordered |
| Code Blocks | ✅ Working | Syntax highlighting enabled |
| Tables | 🧪 Testing | This table itself |
| Links | ✅ Working | External links supported |
| Images | ❌ Not tested | Would need file upload |

## Mixed Content Example

Here's a complex paragraph that combines multiple elements: **Bold text** with *italic emphasis*, some `inline code`, and a [link to documentation](https://docs.example.com). 

The following code demonstrates how to process this data:

```json
{
  "test": {
    "markdown": true,
    "features": ["headers", "lists", "code", "tables"],
    "status": "testing",
    "timestamp": "2025-06-07T10:30:00Z"
  }
}
```

## Final Notes

This comprehensive test includes:
- All header levels (H1-H4)
- Text formatting (bold, italic, strikethrough)
- Inline and block code with syntax highlighting
- Ordered and unordered lists with nesting
- Blockquotes with nesting
- Tables with alignment
- Links (both inline and reference style)
- Horizontal rules
- Mixed content paragraphs

Please rewrite this entire message back to me with proper formatting to test if the markdown rendering works correctly in your chat application!