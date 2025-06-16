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
    "Small": {
        "fg_color": "#6B4AFF",
        "bg_color": "#2B2B2B",
        "hover_color": "#3D11FF",
        "text_color": "white",
        "corner_radius": 14,
        "font": ("Lato", 20, "bold"),
        "border_width": 0
    }
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
    }
}

# Entry styles (if you want to style entries too)
entry_styles = {
    "default": {
        "fg_color": "#F5F5F5",
        "border_color": "#CCCCCC",
        "corner_radius": 8,
        "text_color": "#333333",
        "font": ("Lato", 28, "bold")
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
    }
}