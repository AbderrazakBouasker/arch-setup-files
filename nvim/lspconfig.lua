-- .config/nvim/lua/configs/  
-- EXAMPLE 
local on_attach = require("nvchad.configs.lspconfig").on_attach
local on_init = require("nvchad.configs.lspconfig").on_init
local capabilities = require("nvchad.configs.lspconfig").capabilities

local lspconfig = require "lspconfig"
local servers = {
  html = { "html", "javascriptreact", "typescriptreact" },
  cssls = { "css", "scss", "less" },
  tsserver = { "javascript", "javascriptreact", "typescript", "typescriptreact" },
  tailwindcss = { "html", "javascript", "javascriptreact", "typescript", "typescriptreact" }
}

-- Set up language servers for each filetype
for server, filetypes in pairs(servers) do
  lspconfig[server].setup {
    on_attach = on_attach,
    on_init = on_init,
    capabilities = capabilities,
    filetypes = filetypes -- Specify the filetypes associated with the server
  }
end
