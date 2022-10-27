let button_menu = document.querySelector("#menu")
let id_routes = document.querySelector("#routes")
let id_sections = document.querySelector("#sections")
let navbar = document.querySelector("#navbar")



function showMenu() {

    button_menu.addEventListener("click", function () {
        navbar.classList.toggle('h-auto')
        navbar.classList.toggle('bg-transparent')
        id_routes.classList.toggle('hidden')
        id_sections.classList.toggle('hidden')
    })
}



function activateMobileMenu() {

    // When resizing the screen

    window.onresize = () => {

        if (window.innerWidth < 800) {

            if (!id_routes.classList.value.includes('hidden')) {

                navbar.classList.toggle('h-auto')
                navbar.classList.toggle('bg-transparent')
                id_routes.classList.toggle('hidden')
                id_sections.classList.toggle('hidden')
            };

        } else {
            navbar.classList.remove('h-auto')
            navbar.classList.remove('bg-transparent')
            id_routes.classList.remove('hidden')
            id_sections.classList.remove('hidden')
        }
    };


    // when refreshing the page

    if (window.innerWidth < 800) {

        if (!button_menu.classList.value.includes('active')) {
            navbar.classList.toggle('h-auto')
            navbar.classList.toggle('bg-transparent')
            id_routes.classList.toggle('hidden')
            id_sections.classList.toggle('hidden')
        }
    }
}


showMenu()
activateMobileMenu()