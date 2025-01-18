# AJAX Flask Examples

This repository demonstrates how to use AJAX with Flask through two examples using XMLHttpRequest (classic approach).
For a modern implementation using the Fetch API, see [Flask Fetch Examples](https://github.com/eniompw/FlaskFetch).

## 1. Hello Name Example
A simple interactive example that updates text without page reload.

### Components:
* Frontend: [`templates/ajax.html`](templates/ajax.html)
  * Uses XMLHttpRequest to make AJAX calls
  * Handles Enter key press for better UX
  * Updates page content dynamically
* Backend: [`flask_app.py`](flask_app.py)
  * Simple Flask route that returns personalized greeting

### Key Features:
* Real-time updates without page refresh
* Enter key support
* Simple demonstration of GET parameters

## 2. Stock Ticker Example
An automatic stock price updater for HSBC stock.

### Components:
* Frontend: [`templates/stock.html`](templates/stock.html)
  * Auto-updates every 2 seconds
  * Uses XMLHttpRequest for periodic updates
* Backend: [`stock.py`](stock.py)
  * Fetches real-time stock data from Yahoo Finance
  * Parses and extracts current stock price

### Key Features:
* Automatic updates using setInterval
* Real-time stock price data
* Web scraping implementation

## Technical Notes

### AJAX Implementation:
* Uses vanilla JavaScript XMLHttpRequest
* No external JavaScript libraries required
* Asynchronous updates without page reload

### Frontend Tips:
* `<button>` is used instead of `<input type="submit">` for cleaner code
* Forms are intentionally avoided to prevent page reloads
* Event listeners handle both click and Enter key events

### Backend Tips:
* Flask routes handle AJAX requests
* Request parameters accessed via `request.args`
* Simple response handling

## Setup and Running
1. Install Flask: `pip install flask requests`
2. Run either example:
   * Hello Name: `python flask_app.py`
   * Stock Ticker: `python stock.py`

## Additional Resources
* [More Dynamic Flask Examples](https://github.com/eniompw/DynamicFlask)

## References
* [W3Schools AJAX Tutorial](https://web.archive.org/web/20210607235923/https://www.w3schools.com/js/js_ajax_intro.asp)
* [W3Schools Enter Key Events](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_trigger_button_enter)
* [W3Schools JavaScript Timing](https://www.w3schools.com/js/js_timing.asp)
* [Flask Request Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object)
