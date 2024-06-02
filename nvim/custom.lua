-- .config/nvim/lua/plugins/
local plugins = {
  { "github/copilot.vim", lazy = true, keys = {
    { "<leader>cpl", desc = "Load Copilot" }
  } },
  {
    { "windwp/nvim-ts-autotag", lazy = false, opts = {
      enable_close = true,
      enable_rename = true,
      enable_close_on_slash = false,
    } }
  },
  { "smoka7/hop.nvim",
    opts={
      multi_windows = true,
      keys = "htnsueoaidgcrlymbkjvx",
      uppearace_labels = true,
    },
    keys = {
      {
        "<leader>fj",
        desc = "hop to word",
        function ()
          require("hop").hint_words()
        end,
        mode = {"n","x","o"},
      }
    }
  }
}
return plugins
