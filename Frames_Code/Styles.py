# styles.py

# Button style dictionary
button_styles = {
    "Big": {
        "fg_color": "#4A90E2",
        "bg_color": "#2B2B2B",
        "hover_color": "#00cbff",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Lato", 40, "bold"),
        "border_width": 0
    },
    "Medium": {
        "fg_color": "#8FFFEC",
        "bg_color": "#2B2B2B",
        "hover_color": "#30FFDC",
        "text_color": "#242323",
        "corner_radius": 14,
        "font": ("Lato", 20, "bold"),
        "border_width": 0
    },
    "Danger!": {
        "fg_color": "#CF0808",
        "bg_color": "#2B2B2B",
        "hover_color": "#C70000",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Segoe UI", 20, "bold"),
        "border_width": 0
    },
    "Small": {
        "fg_color": "#6B4AFF",
        "bg_color": "#2B2B2B",
        "hover_color": "#3D11FF",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Lato", 20, "bold"),
        "border_width": 0
    },
    "First": {
        "fg_color": "#FFAA4D",
        "bg_color": "#2B2B2B",
        "hover_color": "#C1733B",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Arial", 20, "bold"),
        "border_width": 0
    },
    "Second": {
        "fg_color": "#4A8AE8",
        "bg_color": "#2B2B2B",
        "hover_color": "#2F69B8",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Arial", 20, "bold"),
        "border_width": 0
    },
    "Third": {
        "fg_color": "#32C766",
        "bg_color": "#2B2B2B",
        "hover_color": "#28A957",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Arial", 20, "bold"),
        "border_width": 0
    },
    "Fourth": {
        "fg_color": "#9FA8DA",  # Soft blue
        "hover_color": "#8894C7",
        "bg_color": "#2B2B2B",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Lato", 20, "bold"),
        "border_width": 0
    },
    "Quick": {
        "fg_color": "#9FA8DA",
        "bg_color": "#2B2B2B",
        "hover_color": "#8894C7",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Arial", 10, "bold"),
        "border_width": 0
    },
}

# Label styles
label_styles = {
    "title1": {
        "text_color": "#c4c364",
        "corner_radius": 3,
        "font": ("Lato", 48, "bold")
    },
    "title2": {
        "text_color": "#e4e4e4",
        "corner_radius": 3,
        "font": ("Lato", 40, "bold")
    },
    "subtitle": {
        "text_color": "#c4c364",
        "corner_radius": 3,
        "font": ("Lato", 20, "bold")
    },
    "subtitle2": {
        "text_color": "#e4e152",
        "corner_radius": 3,
        "font": ("Lato", 25, "bold"),
        "fg_color": "transparent"
    },
    "error_title": {
        "text_color": "#FF0000",
        "corner_radius": 3,
        "font": ("Lato", 14, "bold")
    },
    "Question": {
        "text_color": "#D0FF00",
        "corner_radius": 8,
        "font": ("Lato", 32, "bold")
    },
    "Menu_title": {
        "text_color": "#5D9CEC",
        "corner_radius": 8,
        "font": ("Segoe UI", 32, "bold")
    },
    "Menu_subtitle": {
        "text_color": "#DDC704",
        "corner_radius": 8,
        "font": ("Arial", 32, "bold")
    },
    "Menu_Labels2": {
        "text_color": "#5D9CEC",
        "corner_radius": 8,
        "font": ("Segoe UI", 20, "bold")
    },
    "Menu_Labels": {
        "text_color": "#398FFF",
        "corner_radius": 8,
        "font": ("Segoe UI", 16, "bold")
    },
    "Menu_Labels_Tiny": {
        "text_color": "#398FFF",
        "corner_radius": 8,
        "font": ("Segoe UI", 12, "bold")
    },
    "Top_Labels": {
        "text_color": "#1A9FB1",
        "corner_radius": 8,
        "font": ("Segoe UI", 20, "bold")
    },
    "Tiny_Labels": {
        "text_color": "#4EF737",
        "corner_radius": 8,
        "font": ("Segoe UI", 14, "bold")
    },
    "Tiny_Labels2": {
        "text_color": "#4EF737",
        "corner_radius": 8,
        "font": ("Segoe UI", 12, "bold")
    },
}

# Entry styles (if you want to style entries too)
entry_styles = {
    "default": {
        "fg_color": "#F5F5F5",
        "border_color": "#CCCCCC",
        "corner_radius": 8,
        "text_color": "#333333",
        "font": ("Lato", 28, "bold")
    },
    "Query": {
        "fg_color": "#F5F5F5",
        "border_color": "#CCCCCC",
        "corner_radius": 8,
        "text_color": "#333333",
        "font": ("Lato", 18, "bold")
    }
}

checkBox = {
    "Box1": {
        "hover_color": "#0FE4D2",
        "bg_color": "#6200FF",
        "corner_radius": 5,
        "fg_color": "#37ADA7",
        "border_width": 0,
    }
}
ComboBox = {
    "Box1": {
        "state": "readonly",
        "border_color": "#4A90E2",
        "bg_color": "#2B2B2B",
        "dropdown_fg_color": "#2B2B2B",
        "dropdown_text_color": "white",
        "text_color": "white",
        "button_color": "grey",
        "font": ("Lato", 32, "bold"),
        "dropdown_font": ("Lato", 32, "bold")
    },
    "Box2": {
        "state": "readonly",
        "border_color": "#4A90E2",
        "bg_color": "#2B2B2B",
        "dropdown_fg_color": "#2B2B2B",
        "dropdown_text_color": "white",
        "text_color": "white",
        "button_color": "grey",
        "font": ("Lato", 18, "bold"),
        "dropdown_font": ("Lato", 18, "bold")
    }
}

Switches = {
    "Switch1": {
        "switch_width": 50,
        "switch_height": 26,
        "fg_color": "#1A9FB1",
        "progress_color": "#0F6F7F",
        "button_color": "#FFFFFF",
        "button_hover_color": "#E0F7FA",
        "text_color": "#FFFFFF",    # Doesn't matter if text is hidden
        "text": "",                 # Hides the text completely        # Centers the switch nicely
        "corner_radius": 100      # Optional: make it fully rounded
    }
}
