/**
 * @format
 * @type {import('tailwindcss').Config}
 */

export const content = [
  "./templates/**/*.html",
  "./node_modules/tw-elements/js/**/*.js",
];
export const theme = {
  extend: {},
};
export const plugins = [require("tw-elements/plugin.cjs")];
