** Working on it **

** Necessary **

- fix markdown
    - ~~Strikethrough~~ not properly rendered in response and prompt
    - not rendering dots at the start of list items in unordered lists
    - not rendering numbers at the start of list items in ordered lists
- edge case: if, while the response is loading/being streamed, the "cancella" button is hit, then it should also stop the generation
- answer that is generating does not force user to the bottom of the page
- suggestions overflow on mobile without resizing of window text area
- on mobile the markdown for code overflows
- more readable font for code
- less margin on mobile to see more text
- Attach images
- Attach files
    - may have to change to responses api
- Button to stop generation (if you don't like it)
- "&copy" in resulting html. Probably have to consider all possible html escape sequences.
- when a lot of text is in the text area, it deforms and takes up the whole screen. it shouldn't do that. There should be a maximum height for the input text area, and the user should scroll inside it if it gets too big

** Secondary **


- Button to copy the code part of a response
- user should be able to write a prompt while the answer is generating, for it to be sent later, and the text area should be focused right after sending the message
- when you have a single long word it overflows instead of wrapping around
