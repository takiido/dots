local plugin_path = debug.getinfo(1, 'S').source:match("@(.*/)")
for _, file in ipairs(vim.fn.readdir(plugin_path)) do
    if file ~= "init.lua" and file:sub(-4) == ".lua" then
        local module = "plugins." .. file:sub(1, -5)
        require(module)
    end
end
