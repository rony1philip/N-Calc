import { createSystem, defaultConfig } from "@chakra-ui/react";
import { buttonRecipe } from "./button.recipe"; // אם את משתמשת בזה

export const system = createSystem(defaultConfig, {
  globalCss: {
    html: {
      fontSize: "16px",
      height: "100%",
    },
    body: {
      height: "100%",
      fontSize: "25px",
      margin: 0,
      padding: 0,
      fontFamily: "Rubik, sans-serif",
      backgroundColor: "#FAEBD7",
      color: "#212121",
    },
    a: {
      color: "ui.link",
      textDecoration: "none",
      _hover: {
        textDecoration: "underline",
      },
    },
  },

  theme: {
    tokens: {
      colors: {
        ui: {
          main: { value: "#009688" },
          dark: { value: "#00695c" },
          light: { value: "#DDEB9D" },
          background: { value: "#FAEBD7" },
          border: { value: "#e0e0e0" },
          text: { value: "#212121" },
          link: { value: "#212121" }
        },
      },

      fonts: {
        body: { value: "Rubik, sans-serif" },
        heading: { value: "Rubik, sans-serif" },
        mono: { value: "Menlo, monospace" },
      },

      fontSizes: {
        xs: { value: "1.50rem" },
        sm: { value: "1.50rem" },
        md: { value: "1.125rem" },
        lg: { value: "1.5rem" },       // ← תפריט / טקסט רגיל גדול יותר
        xl: { value: "2rem" },         // ← כותרות
        "2xl": { value: "2.5rem" },    // ← כותרות גדולות מאוד
},


      radii: {
        none: { value: "0" },
        sm: { value: "4px" },
        md: { value: "8px" },
        lg: { value: "12px" },
        full: { value: "9999px" },
      },


    },

    recipes: {
      button: buttonRecipe, // אפשר למחוק אם לא בשימוש
    },
  },
});
