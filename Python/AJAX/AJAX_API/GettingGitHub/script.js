fetch("https://api.github.com/users/esokami")
    .then(response => response.json())
    .then(coderData => console.log(coderData))
    .catch(err => console.log(err))

async function getCoderData(){
    var response = await fetch("https://api.github.com/users/esokami");
    var coderData = await response.json();
    getGitUser(coderData.login);
}

function getGitUser(user) {
    document.getElementById("git").innerHTML = `
    <p>${user.login}</p>
    `
}
