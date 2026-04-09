function checkNews() {

    const text = document.getElementById("newsText").value;
 
    if (!text) {
        alert("Please enter some text!");
        return;
    }

    fetch("http://localhost:8080/api/news/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("resultBox").classList.remove("hidden");

        document.getElementById("prediction").innerText =
            "Prediction: " + data.prediction;

        document.getElementById("confidence").innerText =
            "Confidence: " + data.confidence;

            if (data.prediction.includes("Real")) {
    document.getElementById("prediction").style.color = "green";
} else {
    document.getElementById("prediction").style.color = "red";
}
    })
    .catch(error => {
        console.error("Error:", error);
    });
  
}