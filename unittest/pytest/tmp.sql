SELECT ci.club_nbr,
        i.upc_nbr as upc,
        i.item_nbr as item_id,
        i.item_nbr as wm_item_num,
        ci.link_item_nbr,
        ci.unit_retail_amt,
        NVL(TRIM(i.item1_desc), ' ') as item_desc1,
        NVL(TRIM(i.item2_desc), '') as item_desc2,
        i.item_weight_qty,
        i.upc_nbr||'_A' as image,
        i.sell_unit_qty,
        i.sell_unit_uom_code,
        ci.unit_retail_amt as curr_item_price,
        i.dept_nbr as pcs_catg_nbr,
        i.subclass_nbr as pcs_subcatg_nbr,
        i.vendor_stock_id as pcs_model,
        i.item_nbr || ' ' || i.signing_desc as keywords
FROM  dpsamitm.ITEM i, dpsamitm.club_item ci, dpsamitm.club_item_invt civ
WHERE i.item_nbr = ci.item_nbr
        AND i.item_nbr = civ.item_nbr
        AND ci.club_nbr = civ.club_nbr
        AND ci.item_status_code NOT IN ('D', 'R')
        AND ( cast(i.upc_nbr as varchar(11)) like '2%00000'
                --OR i.item_nbr in (QUICK_ITEM_LIST)
                OR civ.on_hand_qty != 0
                OR civ.on_order_qty > 0
            )
        AND ci.unit_retail_amt !=0
        AND ci.club_nbr=6265
