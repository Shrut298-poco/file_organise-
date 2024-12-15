// script.js

// Predefined exchange rates
const exchangeRates = {
    USD: { INR: 82.50, EUR: 0.92, GBP: 0.80 },
    INR: { USD: 0.012, EUR: 0.011, GBP: 0.0097 },
    EUR: { USD: 1.08, INR: 88.80, GBP: 0.87 },
    GBP: { USD: 1.25, INR: 102.50, EUR: 1.15 },
};

// Function to perform conversion
function convertCurrency() {
    const fromCurrency = document.getElementById("from-currency").value;
    const toCurrency = document.getElementById("to-currency").value;
    const amount = parseFloat(document.getElementById("amount").value);
    const resultDiv = document.getElementById("result");

    // Validate input
    if (isNaN(amount) || amount <= 0) {
        resultDiv.innerHTML = "Please enter a valid amount.";
        return;
    }

    if (!exchangeRates[fromCurrency] || !exchangeRates[fromCurrency][toCurrency]) {
        resultDiv.innerHTML = `Conversion from ${fromCurrency} to ${toCurrency} is not supported.`;
        return;
    }

    // Perform conversion
    const rate = exchangeRates[fromCurrency][toCurrency];
    const convertedAmount = (amount * rate).toFixed(2);

    // Display result
    resultDiv.innerHTML = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
}

// Attach event listener to the button
document.getElementById("convert-button").addEventListener("click", convertCurrency);
