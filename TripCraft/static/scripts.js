document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("tripForm").addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Display processing message
        document.getElementById("responseArea").innerHTML = "Processing request...";

        var formData = new FormData(this);

        fetch('/generate', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            console.log("Received response from server:", response);
            return response.json();
        })
        .then(data => {
            console.log("Received data from server:", data);
            // Format and display the response in the response area
            const formattedResponse = formatItinerary(data.response);
            document.getElementById("responseArea").innerHTML = formattedResponse;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("responseArea").innerHTML = 'Error processing request';
        });
    });
});

function formatItinerary(text) {
    // Split the response by lines and process each one
    const lines = text.split('\n');
    return lines.map(line => {
        if (line.startsWith('**')) {
            // Titles
            return `<div class="title">${line.replace(/\*\*/g, '')}</div>`;
        } else if (line.startsWith('* ')) {
            // List items
            return `<li>${line.substring(2)}</li>`; // Remove '* '
        } else {
            // Regular text
            return `<p>${line}</p>`;
        }
    }).join('');
}


