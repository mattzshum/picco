import React, { useEffect } from 'react';
import '../stylesheets/ExternalLinkPanel.css'

const ExternalLinkPanel = ({website, yelp_link}) => {
    useEffect(() =>{
        console.log(website, yelp_link)
    }, []);

    return (
        <div class='el-container'>
            <div class='el-card'>
                <div class='el-contentBx'>
                    <h3>External Links</h3>
                    <ul class='el-info'>
                        <li>{website}</li>
                        <li>{yelp_link}</li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default ExternalLinkPanel;