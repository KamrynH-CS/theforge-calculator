(function () {
    let ores = {};
    let weaponOdds = {};
    let armorOdds = {};
    let weaponVariants = {};

    // Map singular main-weapon names (as they appear in weaponOdds.json) to
    // the category keys used in weaponVariants.json (usually pluralized).
    const categoryMap = {
        "Dagger": "Daggers",
        "Straight Sword": "Straight Swords",
        "Gauntlet": "Gauntlets",
        "Great Sword": "Great Swords",
        "Great Axe": "Great Axes",
        "Katana": "Katanas",
        "Colossal Sword": "Colossal Swords"
    };

    const oreInputs = [
        { nameEl: () => document.getElementById('name1'), amtEl: () => document.getElementById('amt1'), optionsId: 'options1' },
        { nameEl: () => document.getElementById('name2'), amtEl: () => document.getElementById('amt2'), optionsId: 'options2' },
        { nameEl: () => document.getElementById('name3'), amtEl: () => document.getElementById('amt3'), optionsId: 'options3' },
        { nameEl: () => document.getElementById('name4'), amtEl: () => document.getElementById('amt4'), optionsId: 'options4' }
    ];

    const runeInputs = [
        { nameEl: () => document.getElementById('rune1'), amtEl: () => document.getElementById('runeAmt1'), optionsId: '' },
        { nameEl: () => document.getElementById('rune2'), amtEl: () => document.getElementById('runeAmt2'), optionsId: '' },
        { nameEl: () => document.getElementById('rune3'), amtEl: () => document.getElementById('runeAmt3'), optionsId: '' }
    ];

    const rarityValue = document.getElementById('rarity-value');
    const compositionArea = document.getElementById('composition-area');
    const traitsArea = document.getElementById('traits-area');
    const oddsArea = document.getElementById('odds-area');
    const warningEl = document.getElementById('warning');
    const segBtns = document.querySelectorAll('.seg-btn');
    const resultsWrapper = document.getElementById('results-wrapper');
    const oreListEl = document.getElementById('ore-list');
    const rarityMultEl = document.getElementById('combined-multiplier');
    const oreSearchEl = document.getElementById('ore-search');

    let currentCraftType = 'Weapon';
    let debounceTimer = null;

    Promise.all([
        fetch('ores.json').then(r => r.json()),
        fetch('weaponOdds.json').then(r => r.json()),
        fetch('armorOdds.json').then(r => r.json()),
        fetch('weaponVariants.json').then(r => r.json())
    ]).then(([oresData, wOdds, aOdds, wVariants]) => {
        ores = oresData;
        weaponOdds = wOdds;
        armorOdds = aOdds;
        weaponVariants = wVariants;
        initUI();
        renderOreList();
        renderEmptyResults();
    }).catch(err => { console.error(err); showWarning('Failed to load JSON files.') });

    function initUI() {
        const oreNames = Object.keys(ores).sort((a, b) => a.localeCompare(b));

        oreInputs.forEach((row) => {
            const optionsList = document.getElementById(row.optionsId);
            optionsList.innerHTML = '';
            oreNames.forEach(name => {
                const li = document.createElement('li');
                li.textContent = name;
                li.addEventListener('click', () => {
                    row.nameEl().value = name;
                    optionsList.style.display = 'none';
                    doAutoUpdate();
                });
                optionsList.appendChild(li);
            });

            const inputEl = row.nameEl();
            inputEl.addEventListener('input', () => {
                const filter = inputEl.value.toLowerCase();
                let hasVisible = false;
                optionsList.querySelectorAll('li').forEach(li => {
                    if (li.textContent.toLowerCase().includes(filter)) {
                        li.style.display = '';
                        hasVisible = true;
                    } else li.style.display = 'none';
                });
                optionsList.style.display = hasVisible ? 'block' : 'none';
                showOrHideClear(inputEl);
                doAutoUpdateDebounced();
            });

            document.addEventListener('click', e => {
                if (!inputEl.contains(e.target) && !optionsList.contains(e.target)) optionsList.style.display = 'none';
            });

            const clearBtn = row.nameEl().parentElement.querySelector('.clear-btn');
            clearBtn.addEventListener('click', () => {
                inputEl.value = '';
                clearBtn.style.display = 'none';
                optionsList.style.display = 'none';
                doAutoUpdate();
            });

            row.amtEl().addEventListener('input', () => doAutoUpdate());
        });

        runeInputs.forEach(row => {
            row.nameEl().addEventListener('input', doAutoUpdate);
            row.amtEl().addEventListener('input', doAutoUpdate);
        });

        document.querySelectorAll('.num-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = document.getElementById(btn.dataset.target);
                if (!target) return;
                let val = parseInt(target.value) || 0;
                if (btn.classList.contains('plus')) val++;
                else val = Math.max(0, val - 1);
                target.value = val;
                doAutoUpdate();
            });
        });

        segBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                segBtns.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
                btn.classList.add('active');
                btn.setAttribute('aria-selected', 'true');
                currentCraftType = btn.dataset.type || 'Weapon';
                doAutoUpdate();
            });
        });

        oreSearchEl.addEventListener('input', () => renderOreList(oreSearchEl.value));
    }

    function renderOreList(filterText = '') {
        oreListEl.innerHTML = '';
        const sortedOres = Object.entries(ores)
            .sort((a, b) => b[1].multiplier - a[1].multiplier)
            .filter(([name]) => name.toLowerCase().includes(filterText.toLowerCase()));

        sortedOres.forEach(([name, data]) => {
            const li = document.createElement('li');
            li.style.padding = '4px 6px';
            li.style.cursor = 'default';
            li.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
            li.style.display = 'flex';
            li.style.justifyContent = 'space-between';
            li.style.alignItems = 'center';
            li.style.position = 'relative';

            let tooltipLines = [];
            if (Array.isArray(data.traits) && data.traits.length > 0) {
                data.traits.forEach(trait => {
                    if (trait.maxStat) tooltipLines.push(`${trait.maxStat}% ${trait.description}`);
                    else tooltipLines.push(trait.description);
                });
            }

            if (tooltipLines.length > 0) {
                const tooltip = document.createElement('div');
                tooltip.className = 'ore-tooltip';
                tooltip.style.position = 'absolute';
                tooltip.style.top = '100%';
                tooltip.style.left = '50%';
                tooltip.style.transform = 'translateX(-50%)';
                tooltip.style.background = '#222';
                tooltip.style.color = '#fff';
                tooltip.style.padding = '6px 8px';
                tooltip.style.borderRadius = '6px';
                tooltip.style.whiteSpace = 'pre-line';
                tooltip.style.display = 'none';
                tooltip.style.zIndex = '10';
                tooltip.innerText = tooltipLines.join('\n');
                li.appendChild(tooltip);

                li.addEventListener('mouseenter', () => tooltip.style.display = 'block');
                li.addEventListener('mouseleave', () => tooltip.style.display = 'none');
            }

            const nameSpan = document.createElement('span');
            nameSpan.textContent = name;
            if (data.rarityColor) nameSpan.style.color = data.rarityColor;
            li.appendChild(nameSpan);

            const multSpan = document.createElement('span');
            multSpan.textContent = `×${data.multiplier.toFixed(2)}`;
            multSpan.style.color = '#ccc';
            li.appendChild(multSpan);

            oreListEl.appendChild(li);
        });
    }

    function showOrHideClear(inputEl) {
        const clearBtn = inputEl.parentElement.querySelector('.clear-btn');
        clearBtn.style.display = inputEl.value ? 'block' : 'none';
    }

    function doAutoUpdateDebounced() {
        if (debounceTimer) clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => doAutoUpdate(), 160);
    }

    function gatherAllSelectedOres() {
        const selected = {};
        oreInputs.forEach(row => {
            const name = row.nameEl().value.trim();
            const amtRaw = row.amtEl().value;
            const amt = amtRaw === '' ? 0 : parseFloat(amtRaw);
            if (name && !isNaN(amt) && amt > 0) selected[name] = (selected[name] || 0) + amt;
        });
        return selected;
    }

    function doAutoUpdate() {
        const selected = gatherAllSelectedOres();
        const totalCount = Object.values(selected).reduce((a, b) => a + b, 0);

        if (totalCount < 3) {
            renderEmptyResults();
            return;
        }

        const computed = getItemChancesWithTraits(selected, currentCraftType);
        renderResults(computed);
    }

    function renderEmptyResults() {
        resultsWrapper.style.display = 'none';
        rarityValue.textContent = '—';
        rarityMultEl.textContent = 'Mult: ×0.00';
        compositionArea.innerHTML = '<div class="muted">Enter ores to show composition</div>';
        traitsArea.innerHTML = '<div class="muted">Traits will appear here when eligible</div>';
        oddsArea.innerHTML = '<div class="muted">Odds for <strong>' + currentCraftType + '</strong> will appear here when eligible</div>';
    }

    // Try to return a simple fraction for common denominators first (1,2,4,8,16,32,64).
    // If not close to any of those, fall back to a best approximation up to maxDenominator.
    function simpleOrApproxFraction(decimal, maxDenominator = 64) {
        decimal = Math.max(0, Math.min(1, decimal));
        const denominators = [1, 2, 4, 8, 16, 32, 64];
        const EPS = 1e-8;
        for (const d of denominators) {
            const n = Math.round(decimal * d);
            if (Math.abs(decimal - n / d) < EPS) {
                const g = gcd(n, d) || 1;
                return `${n / g}/${d / g}`;
            }
        }
        // fallback to general best approx
        return fraction(decimal, maxDenominator);
    }

    function fraction(decimal, maxDenominator = 100) {
        if (decimal === 1) return "1/1";
        decimal = Math.max(0, Math.min(1, decimal));

        let bestNumerator = 0, bestDenominator = 1, minDiff = Infinity;
        for (let d = 1; d <= maxDenominator; d++) {
            const n = Math.round(decimal * d);
            const diff = Math.abs(decimal - n / d);
            if (diff < minDiff) {
                bestNumerator = n;
                bestDenominator = d;
                minDiff = diff;
            }
        }

        const div = gcd(bestNumerator, bestDenominator) || 1;
        const num = Math.round(bestNumerator / div);
        const den = Math.round(bestDenominator / div);
        // guard against 0/x
        if (num === 0) return `0/1`;
        return `${num}/${den}`;
    }

    function gcd(a, b) {
        a = Math.abs(Math.round(a));
        b = Math.abs(Math.round(b));
        if (!a) return b;
        if (!b) return a;
        while (b) {
            const t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    function renderResults(result) {
        resultsWrapper.style.display = 'block';
        rarityValue.textContent = result.rarity;
        rarityMultEl.textContent = `Mult: ×${result.combinedMultiplier.toFixed(2)}`;

        compositionArea.innerHTML = '';
        traitsArea.innerHTML = '';
        oddsArea.innerHTML = '';

        const compList = document.createElement('div');
        compList.className = 'comp-list';
        for (const [ore, pct] of Object.entries(result.composition)) {
            const row = document.createElement('div');
            row.className = 'comp-row';
            row.innerHTML = `<div class="comp-name">${ore}</div><div class="comp-pct">${pct.toFixed(1)}%</div>`;
            compList.appendChild(row);
        }
        compositionArea.appendChild(compList);

        if (result.traits.length === 0) {
            traitsArea.innerHTML = '<div class="traits-none">No traits transfer</div>';
        } else {
            result.traits.forEach(tr => {
                const tbox = document.createElement('div');
                tbox.className = 'trait-box';
                const title = document.createElement('div');
                title.className = 'trait-title';
                title.textContent = tr.ore || 'Ore';
                tbox.appendChild(title);
                tr.lines.forEach(line => {
                    const p = document.createElement('div');
                    p.className = 'trait-line';
                    p.textContent = line;
                    tbox.appendChild(p);
                });
                traitsArea.appendChild(tbox);
            });
        }

        // Build Odds grid and place variants directly under each weapon row
        if (!result.odds || Object.keys(result.odds).length === 0) {
            oddsArea.textContent = 'No odds data';
            return;
        }

        const grid = document.createElement('div');
        grid.className = 'odds-grid';

        for (const [weaponName, mainChance] of Object.entries(result.odds)) {
            // main row (weapon title + percent)
            const item = document.createElement('div');
            item.className = 'odds-row';
            item.style.flexDirection = 'column'; // stack header + variants
            item.style.alignItems = 'stretch';

            const headerRow = document.createElement('div');
            headerRow.style.display = 'flex';
            headerRow.style.justifyContent = 'space-between';
            headerRow.style.alignItems = 'center';

            const nameDiv = document.createElement('div');
            nameDiv.className = 'odds-name';
            nameDiv.textContent = weaponName;

            const pctDiv = document.createElement('div');
            pctDiv.className = 'odds-pct';
            pctDiv.textContent = `${(mainChance * 100).toFixed(1)}%`.replace(/\.0%$/, '%');

            headerRow.appendChild(nameDiv);
            headerRow.appendChild(pctDiv);
            item.appendChild(headerRow);

            // if weapon variants exist and craft type is weapon, add a nested list
            if (currentCraftType === 'Weapon') {
                const categoryKey = categoryMap[weaponName];
                if (categoryKey && weaponVariants[categoryKey]) {
                    const ul = document.createElement('ul');
                    ul.style.listStyle = 'none';
                    ul.style.paddingLeft = '12px';
                    ul.style.margin = '8px 0 0 0';
                    // iterate variants in the category
                    const catObj = weaponVariants[categoryKey];
                    Object.keys(catObj).forEach(variantName => {
                        const variantEntries = catObj[variantName];
                        variantEntries.forEach(v => {
                            const li = document.createElement('li');
                            li.style.padding = '2px 0';

                            const frac = simpleOrApproxFraction(typeof v.chance === 'number' ? v.chance : 1, 64);

                            // ensure multiplier valid
                            let cm = Number(result.combinedMultiplier);
                            if (!isFinite(cm) || cm <= 0) cm = 1;

                            // scaled damage
                            const scaledDmg = (v.dmg * (cm * 2)).toFixed(2);

                            // DPS = damage / time
                            const dps = (scaledDmg / v.time).toFixed(2);

                            // debug output
                            console.debug(`[VariantScale] ${weaponName} > ${variantName}: base=${v.dmg} cm=${cm} scaled=${scaledDmg} time=${v.time} dps=${dps}`);

                            // final displayed line
                            li.textContent = `${variantName} ${frac} — ${scaledDmg} DMG | ${v.time} Cycle's/Attack | ${dps} DPS`;

                            ul.appendChild(li);
                        });

                    });
                    item.appendChild(ul);
                } else {
                    // no variants - optionally show nothing (keeps UI compact)
                }
            }

            grid.appendChild(item);
        }

        oddsArea.appendChild(grid);
    }

    function calculateCombinedMultiplier(selectedOres) {
        let totalMultiplier = 0, totalCount = 0;
        for (const [ore, count] of Object.entries(selectedOres)) {
            if (!ores[ore]) continue;
            totalMultiplier += ores[ore].multiplier * count;
            totalCount += count;
        }
        return totalCount ? totalMultiplier / totalCount : 0;
    }

    function calculateTransferredStat(x) {
        let y = 4.5 * x - 35; if (y < 0) y = 0; if (y > 100) y = 100; return y / 100;
    }

    function getItemChancesWithTraits(selectedOres, craftType = "Weapon") {
        const oddsDict = craftType === "Weapon" ? weaponOdds : armorOdds;
        const combinedMultiplier = calculateCombinedMultiplier(selectedOres);
        const totalCount = Object.values(selectedOres).reduce((a, b) => a + b, 0);
        const MAX_ODDS_ORE_COUNT = 55;
        const oddsKey = totalCount > MAX_ODDS_ORE_COUNT ? MAX_ODDS_ORE_COUNT : totalCount;
        const odds = oddsDict[oddsKey];

        if (!odds) {
            console.warn(`Odds for key ${oddsKey} not found in ${craftType} odds JSON`);
        }

        const composition = {};
        for (const [ore, count] of Object.entries(selectedOres)) composition[ore] = count / totalCount * 100;

        const traits = [];
        for (const [oreName, pct] of Object.entries(composition)) {
            const oreData = ores[oreName];
            if (!oreData || !Array.isArray(oreData.traits)) continue;
            if (oreData.traitType !== "All" && oreData.traitType !== craftType) continue;
            if (pct < 10) continue;

            const transferredFraction = calculateTransferredStat(pct);
            const oreTraitParts = [];
            for (let i = 0; i < oreData.traits.length; i++) {
                const t1 = oreData.traits[i];
                if (typeof t1.maxStat !== "number") continue;
                let line = `${(transferredFraction * t1.maxStat).toFixed(2)}% ${t1.description}`;
                const shouldMerge = t1.description.trim().match(/(with|of|for|per|to|in)$/i)
                    && oreData.traits[i + 1] && typeof oreData.traits[i + 1].maxStat === "number";
                if (shouldMerge) {
                    const t2 = oreData.traits[i + 1];
                    line += ` ${(transferredFraction * t2.maxStat).toFixed(2)}% ${t2.description}`;
                    i++;
                }
                oreTraitParts.push(line);
            }
            if (oreTraitParts.length) traits.push({ ore: oreName, lines: oreTraitParts });
        }
        if (!traits.length) traits.push({ ore: '', lines: [] });

        const highestOre = Object.entries(composition).reduce((a, b) => b[1] > a[1] ? b : a, ["", 0])[0];
        const rarity = ores[highestOre]?.rarity || "Unknown";

        const sortedOdds = Object.fromEntries(
            Object.entries(odds || {}).filter(([k, v]) => v > 0).sort((a, b) => b[1] - a[1])
        );

        return { composition, traits, combinedMultiplier, odds: sortedOdds, rarity };
    }

    function showWarning(msg) { warningEl.style.display = 'block'; warningEl.textContent = '⚠️ ' + msg; }
    function hideWarning() { warningEl.style.display = 'none'; warningEl.textContent = ''; }

})();
