import { createSystem, defaultConfig } from "@chakra-ui/react";
import { buttonRecipe } from "./button.recipe"; // אם את משתמשת בזה

export const system = createSystem(defaultConfig, {
  globalCss: {
    html: {
      fontSize: "16px",
      direction: "rtl", // תמיכה בעברית
    },
    body: {
      fontSize: "14px",
      margin: 0,
      padding: 0,
      fontFamily: "Rubik, sans-serif",
      backgroundColor: "#FFFBDE",
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
          light: { value: "#e0f2f1" },
          background: { value: "#f7f9fc" },
          border: { value: "#e0e0e0" },
          text: { value: "#212121" },
          link: { value: "#1976d2" }
        },
      },

      fonts: {
        body: { value: "Rubik, sans-serif" },
        heading: { value: "Rubik, sans-serif" },
        mono: { value: "Menlo, monospace" },
      },

      fontSizes: {
        xs: { value: "0.75rem" },
        sm: { value: "0.875rem" },
        md: { value: "1rem" },
        lg: { value: "1.125rem" },
        xl: { value: "1.25rem" },
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
