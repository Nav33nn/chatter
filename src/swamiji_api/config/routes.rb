Rails.application.routes.draw do
    # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
      get 'contracts' => 'contracts#fetch_risk_score'
      get 'api/get_search_keys' => 'contracts#fetch_risk_score'
end
