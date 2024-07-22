function autocomplete(input, suggestions) {
    let currentFocus;
    input.addEventListener("input", function() {
        const val = this.value;
        closeAllLists();
        if (!val) return false;
        currentFocus = -1;
        const list = document.createElement("div");
        list.setAttribute("id", this.id + "autocomplete-list");
        list.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(list);
        for (let i = 0; i < suggestions.length; i++) {
            if (suggestions[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                const item = document.createElement("div");
                item.innerHTML = "<strong>" + suggestions[i].substr(0, val.length) + "</strong>";
                item.innerHTML += suggestions[i].substr(val.length);
                item.innerHTML += "<input type='hidden' value='" + suggestions[i] + "'>";
                item.addEventListener("click", function() {
                    input.value = this.getElementsByTagName("input")[0].value;
                    closeAllLists();
                });
                list.appendChild(item);
            }
        }
    });
    input.addEventListener("keydown", function(e) {
        const x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            currentFocus++;
            addActive(x);
        } else if (e.keyCode == 38) {
            currentFocus--;
            addActive(x);
        } else if (e.keyCode == 13) {
            e.preventDefault();
            if (currentFocus > -1) {
                if (x) x[currentFocus].click();
            }
        }
    });

    function addActive(x) {
        if (!x) return false;
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = x.length - 1;
        x[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(x) {
        for (let i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists(elmnt) {
        const items = document.getElementsByClassName("autocomplete-items");
        for (let i = 0; i < items.length; i++) {
            if (elmnt != items[i] && elmnt != input) {
                items[i].parentNode.removeChild(items[i]);
            }
        }
    }

    document.addEventListener("click", function(e) {
        closeAllLists(e.target);
    });
}