<script>("themeSelector").addEventListener("change", function() {let = selectedTheme = this.value}
    const body = document.getElementById("body");

    // Remove all theme classes  
    body.classList.remove("light", "dark", "ocean", "forest");

    // Add the selected theme class  
    body.classList.add(selectedTheme);  
        });

    // Set default theme  
    document.getElementById("themeSelector").value = "light";
    document.getElementById("body").classList.add("light");
</script>;
