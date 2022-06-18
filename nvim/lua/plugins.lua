return require('packer').startup(function()

    -- Packer can manage itself as an optional plugin
    use {'wbthomason/packer.nvim', opt = true}

    -- Startify
    use { 'mhinz/vim-startify' }

    -- Devicons
    use { 'ryanoasis/vim-devicons' }

    -- Color scheme
    use { 'sainnhe/gruvbox-material' }
    use { 'ghifarit53/tokyonight-vim' }

    -- Fuzzy finder
    use {
        'nvim-telescope/telescope.nvim',
        requires = {{'nvim-lua/popup.nvim'}, {'nvim-lua/plenary.nvim'}}
    }

    -- Comments
    use { 'tpope/vim-commentary' }

    --Indent lines
    use { 'Yggdroot/indentLine' }

    -- Nerd Tree
    use { 'preservim/nerdtree' }

    -- Treesitter
    -- use { 'nvim-treesitter/nvim-treesitter' }

    -- Dense Analysis
    use { 'dense-analysis/ale' }

    -- Vim Polyglot
    use { 'sheerun/vim-polyglot' }

    -- Lua development
    use { 'tjdevries/nlua.nvim' }

    -- Vim dispatch
    use { 'tpope/vim-dispatch' }

    -- Fugitive for Git
    use { 'tpope/vim-fugitive' }

    -- Airline
    use { 'vim-airline/vim-airline' }
    use { 'vim-airline/vim-airline-themes' }

    -- AutoCompletion
    use 'neovim/nvim-lspconfig' -- Collection of configurations for built-in LSP client
    use 'hrsh7th/nvim-cmp' -- Autocompletion plugin
    use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp
    use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp
    use 'L3MON4D3/LuaSnip' -- Snippets plugin

end)
