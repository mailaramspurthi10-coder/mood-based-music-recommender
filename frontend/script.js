async function getSongs() {

    let mood = document.getElementById("mood").value;

    let response = await fetch(`http://127.0.0.1:5000/recommend/${mood}`);

    let data = await response.json();

    let output = "";

    data.forEach(song => {
        output += `<p>🎵 ${song.title} - ${song.artist}</p>`;
    });

    document.getElementById("result").innerHTML = output;
}