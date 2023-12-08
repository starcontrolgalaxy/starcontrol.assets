//https://realpython.com/flask-javascript-frontend-for-rest-api/
function getData(endpoint, callback) {
    //replace with fetch api
    //https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
            callback(request.response);
            }
        };

    request.open("GET", endpoint);
    request.send();
}

class ExplorerController {
    constructor() {
        this.explorerView = document.querySelector(".explorer-view");
        this.clearButton = this.explorerView.querySelector("button[data-action='clear']");
        this.clearButton.addEventListener(
            "click",
            this.handleClearClick.bind(this)
        );

        
        this.readButton = this.explorerView.querySelector("button[data-action='read']");
        this.readButton.addEventListener(
            "click", 
            this.handleReadClick.bind(this)
        );
    }

    handleReadClick(event) {
        event.preventDefault();
        console.log('READING DATA')
        let endpoint = 'api/data';
        getData(endpoint, this.showResponse);
    }

    handleClearClick(event) {
        event.preventDefault();
        let code = document.querySelector("code");
        code.innerText = "";
    }

    showResponse(data) {
        const explorerView = document.querySelector(".explorer-view");
        let code = explorerView.querySelector("code");
        code.innerText = data;
    }
}

new ExplorerController();