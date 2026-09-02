Get-Content hashes_list.md5 | ForEach-Object {
    $parts = $_ -split "  "
    $expected = $parts[0]
    $file = $parts[1]

    if (Test-Path $file) {
        $actual = (Get-FileHash $file -Algorithm MD5).Hash.ToLower()
        if ($actual -eq $expected.ToLower()) {
            Write-Host "$file OK"
        } else {
            Write-Host "$file FAILED"
        }
    } else {
        Write-Host "$file NOT FOUND"
    }
}