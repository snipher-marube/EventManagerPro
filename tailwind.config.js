/**
 * @format
 * @type {import('tailwindcss').Config}
 */

export const content = [
  "./templates/**/*.html",
  "./node_modules/flowbite/**/*.js",
];
export const theme = {
  extend: {},
};
export const plugins = [require("flowbite/plugin")];
