import requests

uploadedPartIds = ['/ambry-video/signedId/AQL6WGzPDvQpYQAAAYmW9DzDJz1uKn75UJoPXh2Y5HoGs1WmPHSCidVh02N1nky9RtMgdrElrWDlATUDWCO5-uz7JURVhWEX4_2WojcJLNrZ1jzkhkeRR8EZnA3zIbkFkDVynfQFw7HW4Xaz4qTt6Z_w12MZYGtOs00qN0-SaciCZs1S0yHAYhj1YUkTBIayZjU3L8NDYOEydS3-X2o-Rny6Y6hmX7MPfsifZWkgnsjQBX_0KzZVuT5-PyrUeuYfphySAlB2sOU.bin', '/ambry-video/signedId/AQIW0I9cI0a3EgAAAYmW9Fq_xSvCsNyW5V81ornIE5bloMQCUdlEoPYbZMvOvjffLtmZ3cEwHEfCaITtPVKgGR4d2fhAdy6JtcCHXnjBh6FIJ8YP3kr10-qkjw-o72tPoURoL4YSQoyp1xY6ezRKkzUb1ofXh1yL-jI2LDcaNV_lvUZDm_Kqiow7DKebMhFt9dASmzlwNWtLAU7Xu5jQWTeTWyMO30C4yIbeOIS4b_YHQ2BHhFICbS6Jjqgvm-OnKnEYwgmCGtg.bin', '/ambry-video/signedId/AQK3oLWurI2k9AAAAYmW9ICWiqzZTGNpQAHFZg0aLda7bC6RBR7IAmrlxAVpf5vrzeBJNDIVZb0tQdfcgJ6K_HFQYNZ-gqLppA5g7-PUKlgIwwXFGW0061L7UCMEsmz5e5JQ4ijI4EraecJ7ewuGWyWO0l3g1NnnrZTUPxxB82sjnvV6W_mqYSkQctxOzSJNPbbHiRXi-aV_w21oZoWB7XsihpDZCrrj5-l1z-v3hvcVUDWhUuA3cAalJ_VPyiqRTo1LafeGj-4.bin', '/ambry-video/signedId/AQJWeZ0Ca0-epgAAAYmW9KIa5qqVk9shnV6U8U3NHs_uSMf7CbfNIVqz3zaxB4Z-Idw11MpYGKh3R_uJev6XfV1WUFm4w0MtIaazkzD5MO1JvkKKKCjRPZ1ifKylDxwThLBIJr9tSnhS5GppL07JxITwFY3k_Y6qOpfn29In4qc0peGoVlLYZmiKZyukvWTwAPCfcV0chfrqxCOlPluojpRivQj-VXwTPudw3t-1fo205nwta9eKRMiagMgKK0kKh6YAjKzCDPg.bin', '/ambry-video/signedId/AQLmYoRwhUlUeAAAAYmW9MhBz5CqdNCyAftMCEo2wqBcvwXU3k61QbOq17_xWlGXSWduRuTJJtdq6Yl6j5H-KdwkFcUj-hzYH-wl-0N43QOHOmjfT16qJUDcVTkrcGIrzT-gbpTMRfslQaN4qMsvTx4NybSrXjW9DmFP-Tti6lk4XgmpQmWX7VmXqEH2LBGmcM-RFKSPQ3XXqEuVUTGq0R95PdIFKGQCPthrVNOqwpa2dZhpplyIcjF3wfnzphUaWNxztFAXHxo.bin', '/ambry-video/signedId/AQIyD8FGdeU0rQAAAYmW9PW8GbhmQWeoVNA7KlTxgrPjahMgCiwM7pLnSWNh6gN9ezP7hXteZ-AHax8TsqPcFwnzYEKq-WYmOs0yQD6YBPC_hLTWEAr9Ln2I9u0k6tQFW0RBZkTfbgBYX9nAaa6dwC7W-N_KS2pCX4gpxXc0hjbzs-YegpbPm6EesJ-RR0_40UwPdCSS6-xxXz1QmGyIIrt5V2jO6KtqxG-VsKPIK6oZSbS8QXq6a-lrMy5EnNpviebyJh0G9ZE.bin', '/ambry-video/signedId/AQI1u57Q50mJNwAAAYmW9RyR8MBAgdV9IiFArS3qLD0yMWSgxL_ZySELqJg2t4dnpdJf8EnvtgoWsjg5eM2IB1WbLiclGiHE_wnpxqgPqAFgPkUXURBA-49RWJsxvxCnbfH1tOs4wOCcBy4degj2SbnS7cczSDgIls63TeW9_tizNrOUp5f7EG694_1P33LyHrU9PhF2XrdeprRF1ZEZOL1-WfYV4a0t--Ag-jQxIlF0cDlvkPprCYJiI6JerVWrvxzmt45hIRA.bin', '/ambry-video/signedId/AQK_rdmF7UFtPgAAAYmW9ULc9WuisdZufGrG_IEP91cDgU9DGVh6k-gtOxmFPZkh_nBVE54eNjuDlfz0panh83NfbFNK_4SmVNFg_EkkKuI2A_h-SBJY3l_ls7fHf5yAzQl7X_cIo3xiCRhQRcnmonaOoJJahOMvh7i1eUM6gcUhlT0QvDP7MjoPDw7yd5F_2P7_cq0_8c_HP5-184srZgmR6GRMtleXMkLkNb6-FRi_UEDBfjGkSCNrB5cV3ktbRiqNptrNXG8.bin', '/ambry-video/signedId/AQJ-oWhbnNnMlwAAAYmW9WpY167sOlCqhVuHj6buQispcGeJ9ldeO1IQBM9TS0h4-8Vwm2hVErPmHwxtYuWH8BhPXWUdprMrYbKc0IKuDsf0zFnhiPo88aZImM0rwsXm0P0sbyBjJyh8SbWGo3NOHevqjf7wx0j6RtPwDUaPwrMdYtU_NgfNqhiUFrA_1u85EUrSnam62Xori2mdIDoSxReLDscmogap5CGr0-cyEpkb9Sr6wTu86f-CLLlWnisP1HMTyIFsVd8.bin', '/ambry-video/signedId/AQILKOavuiaLuwAAAYmW9YghKUbSlIKZrSIB2k0sLsXsOS22-foPpzuCfpuKleSB1X2Ipb-Guk0wVl7riTxuU1kuDyKTfhQoeIuzyEWV-xXaTyS6OrprEgW4JFrIF4zXjmr5OIfvfIBhHpCTWvdHGI8nfxCdgwHFkB0Y8U61oYKyW-2NVZ53BojPkGw698bis41DpMzJr9FcgNn5a25lXEKL6OqUW3e_0TtyRkTf1PDvI7jj9_BI1elHR0L45UEdsBqMdeoS09s.bin', '/ambry-video/signedId/AQLSHNjhPV3n8AAAAYmW9ZPYG3Rq-MHVIrjCPh6wm9SdwTjOnUsLrmp-WahmlqIx3qRH7q-VcpTtDczcyxvtnEOARRH9UROCe7HRF4jSQJiSoeoXP3ImT6K2BLuQVBYj0Dwnc6K6Hk5FQ2LM4sVb6EL3CiUIjvwbwlv6nD-AzgjFP6N-AX9s-UkIUl6okEdxv3lYcgdImV1Md0bGSh180oarLZF2-1v2oGGWZN_bw46JC95TofghgjHp8oFF6wfbFiB3_zSdJr0.bin']

if __name__ == "__main__":
    access_token = "AQX_qX5ti8iEIo5tuuNa2jarpRtxcnylBDR9ylI6oT2sdxLju-lTK8w0RUSFMuo31qIRF_DJ56J9YcA-DPDL1SAX-FYiDiMzgwwoDwJDimoxwHbQKpPrvd0ZdlF7v05Vv0JEG_wg3RaNR2Xt5QlU86GYx9a_-ZolTgA5Env_wkN4wcoUuhPOpxsBNSec5y8cHD9zw7i1RHIm3Tc8bcQN_IxOrX4mLLsgSLrDYrI_dJoWfVv6oBx6JGYCjj_4_AyAyC5o89PHjK7lye5stK9DCgAZ7i2lVeW6PnCmvuR0RAv0Is9-2Q7ZJYBdk09QRPYDJpoczGckdGCfWgqJyUGHvg2Uqmlz4Q"

    url = "https://api.linkedin.com/rest/videos?action=finalizeUpload"

    json_data = {
        "finalizeUploadRequest": {
            "video": 'urn:li:video:D4D10AQGv5IUzIJeXuw',
            "uploadToken": "",
            "uploadedPartIds": uploadedPartIds
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        'LinkedIn-Version': '202306',
        'X-Restli-Protocol-Version': '2.0.0'
    }

    response = requests.post(url, json=json_data, headers=headers)

    print(response.status_code)
    print(response.text)
